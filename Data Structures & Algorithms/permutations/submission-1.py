class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        current = []
        used = set()

        def dfs():
            if len(used) == len(nums):
                res.append(current.copy())
                return

            for num in nums:
                if num not in used:
                    used.add(num)
                    current.append(num)

                    dfs()

                    used.remove(num)
                    current.pop()

        dfs()
        return res