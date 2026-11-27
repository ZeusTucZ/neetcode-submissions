class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(r, c, grid):
            if r < 0 or r >= len(grid):
                return

            if c < 0 or c >= len(grid[r]):
                return

            if grid[r][c] == '0':
                return

            grid[r][c] = '0'

            dfs(r + 1, c, grid)
            dfs(r - 1, c, grid)
            dfs(r, c + 1, grid)
            dfs(r, c - 1, grid)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    dfs(i, j, grid)
                    count += 1

        return count