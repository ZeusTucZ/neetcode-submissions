class Solution:
    def isValid(self, s: str) -> bool:
        open_c = {'(': 0, '[': 1, '{': 2}
        close_c = {')': 0, ']': 1, '}': 2}

        stack = []

        for c in s:
            if c in open_c:
                stack.append(open_c[c])
            else:
                if stack and stack[-1] == close_c[c]:
                    stack.pop()
                else:
                    return False

        if stack:
            return False

        return True