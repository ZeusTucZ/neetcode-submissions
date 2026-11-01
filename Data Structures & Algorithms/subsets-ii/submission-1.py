class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        sublist = []
        def dfs(i):
            if i >= len(nums):
                res.add(tuple(sublist.copy()))
                return
            
            sublist.append(nums[i])
            dfs(i + 1)

            sublist.pop()
            dfs(i + 1)

        dfs(0)
        return [list(subset) for subset in res]