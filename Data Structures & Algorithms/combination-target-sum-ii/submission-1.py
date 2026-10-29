class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        res = []
        sublist = []

        def dfs(i, total):
            if total == target:
                res.append(sublist.copy())
                return

            if i >= len(candidates) or total > target:
                return

            sublist.append(candidates[i])
            dfs(i + 1, total + candidates[i])

            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1

            sublist.pop()
            dfs(i + 1, total)

        dfs(0, 0)
        return res