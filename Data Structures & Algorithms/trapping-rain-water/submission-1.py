class Solution:
    def trap(self, height: List[int]) -> int:
        bars = []
        maxLeft = 0
        maxRight = 0

        water = 0

        for h in height:
            maxLeft = max(maxLeft, h)
            bars.append(maxLeft)

        for i in range(len(height) - 1, -1, -1):
            maxRight = max(maxRight, height[i])
            bars[i] = min(bars[i], maxRight)

        for i in range(len(height)):
            water += bars[i] - height[i]

        return water