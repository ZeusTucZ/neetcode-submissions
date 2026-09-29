class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxWindow = 0
        window = 0
        chars = set()

        l = 0
        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                window -= 1
                l += 1

            chars.add(s[r])
            window += 1
            maxWindow = max(maxWindow, window)

        return maxWindow