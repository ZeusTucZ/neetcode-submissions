class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}
        def dfs(count):
            if count in memo:
                return memo[count]

            if count > n:
                return 0

            if count == n:
                return 1

            result = dfs(count + 1) + dfs(count + 2)
            memo[count] = result
            return result

        return dfs(0)