#!/usr/bin/env python3
"""
Regenerate README.md from the repository contents.

Counts solved problems, breaks them down by difficulty and language, and
rebuilds the solutions index. Run after syncing new solutions:

    python3 scripts/update_readme.py
"""
import os
import re
from collections import Counter

TARGET = 250
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATEGORY_DIRS = ["Arrays & Hashing", "Two Pointers"]
LANG_NAMES = {"py": "Python", "sql": "SQL", "cpp": "C++", "java": "Java", "js": "JavaScript"}
DIFF_ORDER = {"Easy": 0, "Medium": 1, "Hard": 2, "?": 3}


def collect():
    """Return (solved_rows, pending_rows, category_rows)."""
    solved, pending = [], []
    for name in sorted(os.listdir(ROOT)):
        path = os.path.join(ROOT, name)
        readme = os.path.join(path, "README.md")
        if not os.path.isdir(path) or name.startswith(".") or not os.path.exists(readme):
            continue
        html = open(readme, encoding="utf-8", errors="replace").read()
        title = re.search(r'href="(https://leetcode\.com/problems/[^"]+)">([^<]+)</a>', html)
        diff = re.search(r"Difficulty-(Easy|Medium|Hard)", html)
        files = [f for f in os.listdir(path) if f != "README.md" and not f.startswith(".")]
        num = name.split("-")[0]
        row = {
            "num": int(num) if num.isdigit() else 0,
            "dir": name,
            "slug": re.sub(r"^\d+-", "", name),
            "title": title.group(2) if title else name,
            "url": title.group(1) if title else "",
            "diff": diff.group(1) if diff else "?",
            "files": sorted(files),
        }
        (solved if files else pending).append(row)

    category = []
    for cat in CATEGORY_DIRS:
        cpath = os.path.join(ROOT, cat)
        if not os.path.isdir(cpath):
            continue
        for f in sorted(os.listdir(cpath)):
            if f.startswith("."):
                continue
            category.append({"cat": cat, "file": f, "slug": os.path.splitext(f)[0]})
    return solved, pending, category


def langs_of(files):
    exts = {os.path.splitext(f)[1].lstrip(".") for f in files}
    exts.discard("md")
    return sorted(LANG_NAMES.get(e, e.upper()) for e in exts if e)


def bar(done, total, width=28):
    filled = round(width * done / total)
    return "█" * filled + "░" * (width - filled)


def main():
    solved, pending, category = collect()
    unique = {r["slug"] for r in solved} | {c["slug"] for c in category}
    n = len(unique)

    diffs = Counter(r["diff"] for r in solved)
    lang_counter = Counter()
    for r in solved:
        for l in langs_of(r["files"]):
            lang_counter[l] += 1
    lang_counter["C++"] += len(category)

    out = []
    w = out.append

    w("# NeetCode 250\n")
    w("> A personal record of my solutions — kept for my own reference and to track\n"
      "> progress. **Goal: complete all 250 problems during 2026.**\n")
    w("Solutions are my own work, saved as I go. Not a teaching resource, not\n"
      "optimised write-ups — just what I actually submitted.\n")
    w("---\n")

    w("## Progress\n")
    w(f"```\n{bar(n, TARGET)}  {n} / {TARGET}   ({n / TARGET * 100:.1f}%)\n```\n")

    w("| Difficulty | Solved |")
    w("|---|:--:|")
    for d in ("Easy", "Medium", "Hard"):
        w(f"| {d} | {diffs.get(d, 0)} |")
    if category:
        w(f"| *Early solutions (difficulty not recorded)* | *{len(category)}* |")
    w(f"| **Total** | **{n}** |")
    w("")
    w("| Language | Solutions |")
    w("|---|:--:|")
    for l, c in lang_counter.most_common():
        w(f"| {l} | {c} |")
    w("")
    w("---\n")

    w("## Solutions\n")
    w("| # | Problem | Difficulty | Language | Solution |")
    w("|--:|---|---|---|---|")
    for r in sorted(solved, key=lambda r: (DIFF_ORDER[r["diff"]], r["num"])):
        code = [f for f in r["files"] if not f.endswith(".md")]
        link = f"[{r['title']}]({r['url']})" if r["url"] else r["title"]
        files_md = " · ".join(
            f"[`{f}`]({r['dir'].replace(' ', '%20')}/{f.replace(' ', '%20')})" for f in code
        )
        w(f"| {r['num'] or ''} | {link} | {r['diff']} | {', '.join(langs_of(r['files'])) or '—'} | {files_md} |")
    w("")

    if category:
        w("### Early solutions (by topic)\n")
        w("Solved before the sync tool was set up, so these are grouped by NeetCode\n"
          "topic instead of problem number. All C++.\n")
        cur = None
        for c in category:
            if c["cat"] != cur:
                cur = c["cat"]
                w(f"\n**{cur}**\n")
            w(f"- [`{c['file']}`]({c['cat'].replace(' ', '%20')}/{c['file'].replace(' ', '%20')})")
        w("")

    if pending:
        w("---\n")
        w("## Not yet solved\n")
        w("Problem statements synced, solutions not committed yet.\n")
        w("| # | Problem | Difficulty |")
        w("|--:|---|---|")
        for r in sorted(pending, key=lambda r: (DIFF_ORDER[r["diff"]], r["num"])):
            link = f"[{r['title']}]({r['url']})" if r["url"] else r["title"]
            w(f"| {r['num'] or ''} | {link} | {r['diff']} |")
        w("")

    w("---\n")
    w("## How this repo is organised\n")
    w("Two layouts, for historical reasons:\n")
    w("- **`<number>-<problem-slug>/`** — created automatically by the LeetSync\n"
      "  browser extension on each accepted submission. Each holds the problem\n"
      "  statement as `README.md` plus the solution file. Commit messages carry\n"
      "  the runtime and memory percentiles.\n"
      f"- **`Arrays & Hashing/`, `Two Pointers/`** — earlier solutions, added by hand and\n"
      f"  grouped by NeetCode topic ({len(category)} files, all C++).\n")
    w("The numbered folders are tool-managed — new solutions land there automatically,\n"
      "so they are deliberately left flat rather than reorganised by topic.\n")
    w("Regenerate this file after syncing new solutions:\n")
    w("```bash\npython3 scripts/update_readme.py\n```\n")
    w("---\n")
    w("Problem statements are © LeetCode. Solutions are mine.")

    open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
    print(f"README.md regenerated — {n}/{TARGET} solved ({n / TARGET * 100:.1f}%)")
    print(f"  {len(solved)} synced folders, {len(category)} topic-folder files, {len(pending)} pending")


if __name__ == "__main__":
    main()
