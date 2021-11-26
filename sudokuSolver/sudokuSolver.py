# this function will find the row and column that has not been filled yet and represent it with -1
# this function will return the position of the row, col as a tuple
# if there are no empty spaces it will return (None, None)

def findEmpty(puzzle):
    for r in range(9):
        for c in range(9): # range(9) is 0, 1, 2, ... 8
            if puzzle[r][c] == -1:
                return r, c

    return None, None  

# this function will check to see if the guess at point row, col is valid
# i.e. the guess is not already in that row, col
# or 3x3 square that it appears in

def checkValid(puzzle, guess, row, col):
    # check first the row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False # if we've repeated, then our guess is not valid!

    # now the column
    col_vals = []
    for i in range(9):
        col_vals.append(puzzle[i][col])

    if guess in col_vals:
        return False

    # and then the square
    row_start = (row // 3) * 3 # dont want any remainders
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True

def solveSudoku(puzzle):
    # 1: choose an empty spot on the board to make a guess, above function
    # if there no empty spaces left, then we return True since we only allow valid inputs and hence the problem is solved
    row, col = findEmpty(puzzle)

    if row is None:  # this is true if our findEmpty function returns None, None
        return True 
    
    # 2: if there is an empty space, we try every number in range 1-9 for that spot
    for guess in range(1, 10): # range(1, 10) is 1, 2, 3, ... 9
    # 3: if number is valid, it will place it in the position of the empty space
        if checkValid(puzzle, guess, row, col):
            puzzle[row][col] = guess
    # 4: use recursion
            if solveSudoku(puzzle):
                return True
        
    #5: if the guess does not solve the puzzle, or not valid, we backtrack and try a new number
        puzzle[row][col] = -1

    #6: after trying every possible solution, if nothing has worked, it is unsolvable
    return False

if __name__ == '__main__':
    sampleBoard = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solveSudoku(sampleBoard))
    print(sampleBoard)