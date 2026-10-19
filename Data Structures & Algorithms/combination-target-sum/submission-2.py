class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []

        def dfs(i):
            sumCombination = sum(combination)
            if i >= len(nums) or sumCombination > target:
                return

            if sumCombination == target:
                res.append(combination.copy())
                return

            for x in range(i, len(nums)):
                combination.append(nums[x])
                dfs(x)
                combination.pop()

        dfs(0)
        return res