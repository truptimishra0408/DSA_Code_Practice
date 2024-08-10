from typing import List

class Solution:
    def isSafe(self, board: List[List[str]], row: int, col: int, number: int) -> bool:
        # column
        for i in range(len(board)):
            if board[i][col] == str(number):
                return False
        
        # row
        for j in range(len(board[0])):
            if board[row][j] == str(number):
                return False
        
        # grid
        sr = 3 * (row // 3)
        sc = 3 * (col // 3)
        
        for i in range(sr, sr + 3):
            for j in range(sc, sc + 3):
                if board[i][j] == str(number):
                    return False
        
        return True
    
    def helper(self, board: List[List[str]], row: int, col: int) -> bool:
        if row == len(board):
            return True
        
        nrow = 0
        ncol = 0
        
        if col == len(board[0]) - 1:
            nrow = row + 1
            ncol = 0
        else:
            nrow = row
            ncol = col + 1
        
        if board[row][col] != '.':
            if self.helper(board, nrow, ncol):
                return True
        else:
            for i in range(1, 10):
                if self.isSafe(board, row, col, i):
                    board[row][col] = str(i)
                    if self.helper(board, nrow, ncol):
                        return True
                    else:
                        board[row][col] = '.'
        
        return False
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.helper(board, 0, 0)
