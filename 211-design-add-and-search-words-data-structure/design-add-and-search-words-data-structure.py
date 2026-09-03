class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        cur = self.root
        for l in word:
            if l not in cur:
                cur[l] = {"end": False}
            cur = cur[l]
        cur["end"] = True

    def dot_search(self, cur, word: str) -> bool:
        for i in range(len(word)):
            l = word[i]
            if l == ".":
                for k, v in cur.items():
                    if k == "end":
                        continue
                    if self.dot_search(v, word[i+1:]):
                        return True
                return False
            if l not in cur:
                return False
            cur = cur[l]
        return cur["end"]

    def search(self, word: str) -> bool:
        return self.dot_search(self.root, word)