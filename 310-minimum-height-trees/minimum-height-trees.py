class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))

        adj = [set() for _ in range(n)]
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)

        leaves = [i for i in range(n) if len(adj[i]) == 1]
        remaining = n

        while remaining > 2:
            remaining -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                nb = adj[leaf].pop()
                adj[nb].remove(leaf)
                if len(adj[nb]) == 1:
                    new_leaves.append(nb)
            leaves = new_leaves

        return leaves