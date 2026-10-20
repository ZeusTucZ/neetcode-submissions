class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        def dfs(grid, r, c):
            nonlocal area
            if r >= len(grid) or r < 0:
                return

            if c >= len(grid[r]) or c < 0:
                return

            if grid[r][c] == 0:
                return

            grid[r][c] = 0
            area += 1

            dfs(grid, r + 1, c)
            dfs(grid, r - 1, c)
            dfs(grid, r, c + 1)
            dfs(grid, r, c - 1)

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    area = 0
                    dfs(grid, r, c)
                    maxArea = max(maxArea, area)

        return maxArea
