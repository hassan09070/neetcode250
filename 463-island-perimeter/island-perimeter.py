class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # left neighbor (or edge of grid)
                    if c == 0 or grid[r][c-1] == 0:
                        count += 1
                    # right neighbor (or edge of grid)
                    if c == cols - 1 or grid[r][c+1] == 0:
                        count += 1
                    # top neighbor (or edge of grid)
                    if r == 0 or grid[r-1][c] == 0:
                        count += 1
                    # bottom neighbor (or edge of grid)
                    if r == rows - 1 or grid[r+1][c] == 0:
                        count += 1
        return count