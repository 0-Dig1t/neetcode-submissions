class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colCount = defaultdict(set)
        boxCount = defaultdict(set)
        rowCount = defaultdict(set)
        for row in range(len(board)):
            for col in range(len(board[row])):
                curr = board[row][col]
                if curr == '.':
                    continue
                if curr in rowCount[row]:
                    return False
                else:
                    rowCount[row].add(curr)
                if curr in colCount[col]:
                    return False
                else:
                    colCount[col].add(curr)
                if curr in boxCount[(row//3, col//3)]:
                    return False
                else:
                    boxCount[(row//3, col//3)].add(curr)
        return True