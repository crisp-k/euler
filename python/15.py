'''

Starting in the top left corner of a 2*2 grid, and only being
able to move to the right and down, there are exactly 6 routes
to the bottom right corner.


How many such routes are there through a 20*20 grid?
'''
import numpy as np

x, y = 0, 0
xDim, yDim = 2, 2
right, down = y + 1, x - 1

grid = [[0, 0],
        [0, 0]]

grid = np.zeros(shape=(xDim, yDim), dtype=int)

# print(grid)
# print()

grid[y][x] = 1          # Top
grid[y][right] = 2      # Right
grid[down][x] = 3       # Down

# print(grid)
 
numSolutions = 0

def canMove(x, y, xDim, yDim):
    if x+1 > xDim:
        return False
    
    if y+1 > yDim:
        return False
    
    return True


numSolutions = 0


def solution(x, y):

    print(x, y)
    
    while x+1 <= xDim:
        return numSolutions + solution(x+1, y)
    
    while y+1 <= yDim:
        return numSolutions + solution(x, y+1)
    
    if x == (xDim - 1) and y == (yDim - 1):
        return 1
    
    return numSolutions


def solution2():
    x, y = 0, 0
    xDim, yDim = 2, 2

    # while(canMove(x, y, xDim, yDim)):



# print(solution(0, 0))


solCount = 0
def solver(x, y, xDim, yDim, solCount):
    print('X: {} Y:{} solCount: {}'.format(x, y, solCount))

    right, down = [1, 0], [0, 1]
    directions = [right, down]


    for i in range(2):
        
        newX = x + directions[i][0]
        newY = y + directions[i][1]

        if canMove(newX, newY, xDim, yDim):    
            if newX == xDim-1 and newY == yDim-1:
                return 1, solCount + 1
            
            _, solCount = solver(newX, newY, xDim, yDim, solCount)
    
    return 0, solCount


# _, solCount = solver(0, 0, 21, 21, solCount)
# print(solCount)





gridSols = {(0, 0): 1}

def memo(x, y, xDim, yDim, solCount, gridSols):
    up, left = [0, -1], [-1, 0]
    directions = [up, left]



    for i in range(3):
        for j in range(3):

            pair = (i, j)

            # Base Case
            if (i-1 == 0 and j == 0) or (i == 0 and j-1 == 0):
                gridSols[pair] = 1

            if pair in gridSols:
                return solCount + gridSols[pair]
            
            memo(i, j, xDim, yDim, solCount, gridSols)


def quick(xDim, yDim):
    grid = np.ones(shape=(xDim, yDim), dtype=int)

    for y in range(yDim):
        for x in range(xDim):
            grid[y][x] = grid[y-1][x] + grid[x-1][y]


    return grid[-1][-1]
    

# print(quick(20, 20))




'''
    Notes on Pascal:
    
    We need to know the row number (n)
    We need to know the innermost column number (k)

    n = targetGridSize + 1

    if n % 2 == 0:
        k = n / 2
    else:
        k = int(n/2) + 1

    math(n, k)
'''


def mathIsCool(n,k):
    if k == 0 or k == n:
        return 1
    
    x = mathIsCool(n-1, k-1) + mathIsCool(n-1, k)

    return x

targetGridSize = 21

n = targetGridSize + 2

if n % 2 == 0:
    k = n / 2
else:
    k = int(n/2) + 1

# print((mathIsCool(n, k)))


def centralBinomial(n):
    x = np.math.factorial(2 * n) / np.math.factorial(n) ** 2
    
    return x

for i in range(21):
    print(centralBinomial(i))