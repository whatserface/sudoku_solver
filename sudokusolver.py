import numpy as np
from time import time
a = time()
input = np.array([[5,1,7,6,0,0,0,3,4],
                  [2,8,9,0,0,4,0,0,0],
                  [3,4,6,2,0,5,0,9,0],
                  [6,0,2,0,0,0,0,1,0],
                  [0,3,8,0,0,6,0,4,7],
                  [0,0,0,0,0,0,0,0,0],
                  [0,9,0,0,0,0,0,7,8],
                  [7,0,3,4,0,0,5,6,0],
                  [0,0,0,0,0,0,0,0,0]], dtype=np.int64)

def find_possible_nums(sudoku, row, col):
    start_row = row // 3 * 3
    start_col = col // 3 * 3
    return {1, 2, 3, 4, 5, 6, 7, 8, 9} - set(sudoku[start_row:start_row + 3, start_col:start_col + 3].flat) - set(sudoku[row, :]) - set(sudoku[:, col])

def solve(sudoku):
    did_put_smth = False
    for row in range(9):
        for col in range(9):
            if sudoku[row, col] == 0:
                resolutions = find_possible_nums(sudoku, row, col)
                if len(resolutions) == 1:
                    sudoku[row, col] = [_ for _ in resolutions][0]
                    did_put_smth = True
    if did_put_smth:
        if np.any((sudoku == 0)):
            return solve(sudoku)
        else:
            return sudoku, True
    print('Решение не найдено')
    return sudoku, False

print(solve(input))
print(time() - a)