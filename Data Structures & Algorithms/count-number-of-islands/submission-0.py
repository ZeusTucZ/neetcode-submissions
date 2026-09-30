class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def dfs(grid, row, col):
            if row < 0 or row >= len(grid):
                return

            if col < 0 or col >= len(grid[row]):
                return

            if grid[row][col] == '0':
                return
            
            grid[row][col] = '0'

            dfs(grid, row + 1, col)
            dfs(grid, row - 1, col)
            dfs(grid, row, col + 1)
            dfs(grid, row, col - 1)
        

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1':
                    dfs(grid, r, c)
                    count += 1

        return count