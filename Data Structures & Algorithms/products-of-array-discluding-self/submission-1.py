class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1] * len(nums)

        multiplier = 1
        for i in range(len(nums) - 1):
            multiplier *= nums[i]
            products[i + 1] *= multiplier

        multiplier = 1
        for i in range(len(nums) - 1, 0, -1):
            multiplier *= nums[i]
            products[i - 1] *= multiplier

        return products
