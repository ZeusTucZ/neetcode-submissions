class Solution:
    def findMin(self, nums: List[int]) -> int:
        minValue = float('inf')
        
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2

            minValue = min(minValue, nums[m])

            if nums[r] < nums[m]:
                l = m + 1
            else:
                r = m - 1

        return minValue
        