class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]

        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(nums), 0, -1):
            if freq[i]:
                for v in freq[i]:
                    res.append(v)
                    k -= 1
            
            if k == 0:
                break

        return res

