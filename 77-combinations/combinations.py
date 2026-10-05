class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []

        def bt(path, num):
            curr = path.copy()

            for x in range(num, n+1):
                curr.append(x)

                if len(curr) == k:
                    result.append(curr.copy())

                if len(curr) < k:
                    bt(curr, x+1)

                curr = path.copy()

        bt([], 1)
        return result