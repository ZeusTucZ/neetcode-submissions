class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def backtracking(r, c, i, used):
            if i >= len(word):
                return True

            if r < 0 or r >= len(board):
                return False

            if c < 0 or c >= len(board[r]):
                return False
            
            if board[r][c] != word[i]:
                return False
            
            if (r, c) in used:
                return False

            used.add((r, c))
            
            found = backtracking(r + 1, c, i + 1, used) or backtracking(r - 1, c, i + 1, used) or backtracking(r, c + 1, i + 1, used) or backtracking(r, c - 1, i + 1, used)

            used.remove((r, c))

            return found
        
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == word[0]:
                    if backtracking(r, c, 0, set()):
                        return True

        return False
