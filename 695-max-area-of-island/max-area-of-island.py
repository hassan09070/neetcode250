class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        best = 0
        for r0 in range(rows):
            for c0 in range(cols):
                if grid[r0][c0] != 1:
                    continue
                stack = [(r0, c0)]
                grid[r0][c0] = 0          # mark visited when ADDING
                area = 0
                while stack:
                    r, c = stack.pop()
                    area += 1
                    for nr, nc in ((r-1,c), (r+1,c), (r,c-1), (r,c+1)):
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            grid[nr][nc] = 0
                            stack.append((nr, nc))
                best = max(best, area)
        return best