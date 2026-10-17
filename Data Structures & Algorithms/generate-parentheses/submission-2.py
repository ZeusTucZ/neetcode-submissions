class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def backtracking(n, open_p, close_p, res):
            if n == open_p == close_p:
                output.append(res)

            if open_p < n:
                backtracking(n, open_p + 1, close_p, res + "(")

            if open_p > close_p:
                backtracking(n, open_p, close_p + 1, res + ")")

        backtracking(n, 0, 0, "")
        return output