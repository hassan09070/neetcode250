class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0
        while True:
            effected = []
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] != 1:
                        continue
                    if (r > 0 and grid[r-1][c] == 2) or \
                       (r < rows-1 and grid[r+1][c] == 2) or \
                       (c > 0 and grid[r][c-1] == 2) or \
                       (c < cols-1 and grid[r][c+1] == 2):
                        effected.append((r, c))

            if not effected:
                break
            count += 1
            for r, c in effected:
                grid[r][c] = 2

        # any fresh orange left means it's unreachable
        for row in grid:
            if 1 in row:
                return -1
        return count