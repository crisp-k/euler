'''
By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve
this problem by trying every route. 
However, Problem 67, is the same challenge with a triangle containing
one-hundred rows; it cannot be solved by brute force, and requires a 
clever method! ;o)
'''
import numpy as np

r1 =  [75]
r2 =  [95, 64]
r3 =  [17, 47, 82]
r4 =  [18, 35, 87, 10]
r5 =  [20, 4, 82, 47, 65]
r6 =  [19, 1, 23, 75, 3, 34]
r7 =  [88, 2, 77, 73, 7, 63, 67]
r8 =  [99, 65, 4, 28, 6, 16, 70, 92]
r9 =  [41, 41, 26, 56, 83, 40, 80, 70, 33]
r10 = [41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
r11 = [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
r12 = [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
r13 = [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
r14 = [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
r15 = [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]


r = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15]


q1 = [3]
q2 = [7, 4]
q3 = [2, 4, 6]
q4 = [8, 5, 9, 3]
q = [q1, q2, q3, q4]



def createSubTriangle(xs, row, col):
    subTriangle = []

    # Pull top value for triangle
    subTriangle.append(xs[row][col])
    nextRow = row+1
    leftElement = col
    rightElement = col + 1


    nextRow = [xs[nextRow][leftElement], xs[nextRow][rightElement]]

    subTriangle.append(nextRow)

    return subTriangle


def maximumPath(tri):
    top = tri[0]
    left = tri[1][0]
    right = tri[1][1]

    leftStep = top + left
    rightStep = top + right

    if leftStep > rightStep:
        return leftStep, left, 0
    else:
        return rightStep, right, 1

def bottomUpPaths(fullTri):
    sol = 0
    numRows = len(fullTri) - 1
    currentRow = numRows
    nextRow = currentRow - 1 

    
    subTris = []

    # Create subTris
    for i in range(len(fullTri[nextRow])):
        subTri = createSubTriangle(fullTri, nextRow, i)
        subTris.append(subTri)

    subPaths = []
    for sub in subTris:
        print(sub)
        step, _, _ = maximumPath(sub)
        subPaths.append ((step))



    print('subTris', subTris)
    print('subPaths', subPaths)

    nextTriangle = fullTri[:nextRow]
    print('Before new row', nextTriangle)

    newRow = []

    for path in subPaths:
        newRow.append(path)

    print('newRow', newRow)

    nextTriangle.append(newRow)
    print(nextTriangle)    
    
    return nextTriangle, subPaths


def solve(tri):
    maxPaths = []
    currentTri = tri

    subTriangle, subPaths = bottomUpPaths(currentTri)
    maxPaths.append(subPaths)
    print(len(subTriangle))

    
    while len(subTriangle) > 1:
        currentTri = subTriangle
        subTriangle, subPaths = bottomUpPaths(currentTri)
        maxPaths.append(subPaths)
        print(len(subTriangle))

    print('maxPaths', maxPaths)

    return


testR = r[:6]
print(testR)
solve(r)