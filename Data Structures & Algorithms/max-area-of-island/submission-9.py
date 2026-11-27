class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        def dfs(r, c, grid):
            if r < 0 or r >= len(grid):
                return 0

            if c < 0 or c >= len(grid[r]):
                return 0

            if grid[r][c] == 0:
                return 0

            grid[r][c] = 0

            return (1 + dfs(r + 1, c, grid) + dfs(r - 1, c, grid) + dfs(r, c + 1, grid) + dfs(r, c - 1, grid))
                        

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    area = dfs(i, j, grid)
                    max_area = max(max_area, area)

        return max_area