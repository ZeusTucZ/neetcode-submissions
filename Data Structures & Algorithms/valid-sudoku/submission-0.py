class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = set()
        col = set()
        box = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[r])):
                nine = (r // 3, c // 3)

                if board[r][c] in row or board[c][r] in col or board[r][c] in box[nine]:
                    return False

                if board[r][c] != '.':
                    row.add(board[r][c])
                    box[nine].add(board[r][c])
                
                if board[c][r] != '.':
                    col.add(board[c][r])

            row = set()
            col = set()

        return True