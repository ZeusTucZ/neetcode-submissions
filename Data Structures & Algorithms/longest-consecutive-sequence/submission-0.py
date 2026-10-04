class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        
        maxCount = 0
        for n in nums:
            if n - 1 in set_nums:
                continue

            count = 0
            while n in set_nums:
                count += 1
                n += 1
            
            maxCount = max(maxCount, count)

        return maxCount
