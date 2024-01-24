""" 
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.

"""

from collections import Counter

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        def is_valid(unit):
            count = Counter(unit)
            for num, freq in count.items():
                if num != '.' and freq > 1:
                    return False
            return True 
        

        for row in board:
            if not is_valid(row):
                return False 
            
        transposed = list(map(list, zip(*board)))
        for col in transposed:
            if not is_valid(col):
                return False
            
        for i in range(0,9,3):
            for j  in range(0,9,3):
                sub_box = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not is_valid(sub_box):
                    return False 
                
        return True