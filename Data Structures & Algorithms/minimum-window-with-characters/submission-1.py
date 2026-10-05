class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = {}
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)

        need = len(count_t)
        have = 0
        minLength = float('inf')
        window = ""
        count_s = {}

        l = 0
        for r in range(len(s)):
            if s[r] not in count_t:
                continue
            
            count_s[s[r]] = 1 + count_s.get(s[r], 0)

            if count_s[s[r]] == count_t[s[r]]:
                have += 1

            while have == need:
                if (r - l + 1) < minLength:
                    minLength = r - l + 1
                    window = s[l:r + 1]

                if s[l] not in count_t:
                    l += 1
                    continue
                
                count_s[s[l]] -= 1

                if count_s[s[l]] < count_t[s[l]]:
                    have -= 1

                l += 1

        return window
                