class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0

        l = 0
        for r in range(len(prices)):
            if l == r:
                continue
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r

        return maxP