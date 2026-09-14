from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colMap = defaultdict(set)
        # check rows and cols
        for r in range(9):
            rowSeen = set()
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in rowSeen:
                    return False
                elif board[r][c] in colMap[c]:
                    return False
                colMap[c].add(board[r][c])
                rowSeen.add(board[r][c])
            
        # check boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                boxSeen = set()
                for r in range(3):
                    for c in range(3):
                        if board[i+r][j+c] == '.':
                            continue
                        if board[i+r][j+c] in boxSeen:
                            return False
                        boxSeen.add(board[i+r][j+c])

        return True