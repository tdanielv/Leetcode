class Solution:
    def solveSudoku(self, board):
        l1, l2, l3, l4, l5, l6, l7, l8, l9 = [],[],[],[],[],[],[],[],[]
        for i in board:
            print(i)
        return board

print(Solution().solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))