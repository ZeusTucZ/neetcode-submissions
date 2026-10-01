class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numberIslands = 0

        def dfs(grid, r, c):
            if r < 0 or r >= len(grid):
                return
            
            if c < 0 or c >= len(grid[r]):
                return
            
            if grid[r][c] == '0':
                return

            grid[r][c] = '0'

            dfs(grid, r - 1, c)
            dfs(grid, r + 1, c)
            dfs(grid, r, c + 1)
            dfs(grid, r, c - 1)

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1':
                    dfs(grid, r, c)
                    numberIslands += 1

        return numberIslands