class Solution:
    def isValid(self, s: str) -> bool:
        open_c = {'(': 0, '{': 1, '[': 2}
        close_c = {')': 0, '}': 1, ']': 2}
        stack = []

        for b in s:
            if b in open_c:
                stack.append(b)
            else:
                if stack and open_c[stack[-1]] == close_c[b]:
                    stack.pop()
                else:
                    return False

        if stack:
            return False
        return True