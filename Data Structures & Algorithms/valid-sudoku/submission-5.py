class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        square_check = [
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
        ]
        for i in range(0,9):
            row_check = {}
            col_check = {}
            for k in range(0,9):
                if board[i][k] != ".":
                    row_check[board[i][k]] = row_check.get(board[i][k], 0) + 1
                    square_check[(i//3)*3+(k//3)][board[i][k]] = square_check[(i//3)*3+(k//3)].get(board[i][k], 0) + 1
                if board[k][i] != ".":
                    col_check[board[k][i]] = col_check.get(board[k][i], 0) + 1
            if any(v > 1 for v in row_check.values()): return False
            if any(v > 1 for v in col_check.values()): return False 
        for i in range(0,9):
            if any(v > 1 for v in square_check[i].values()): return False
        return True                                                                            