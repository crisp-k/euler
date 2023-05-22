'''
In the 20*20 grid below, four numbers along a diagonal line
have been marked in red.

The product of these numbers is 26 * 63 * 78 * 14 = 1788696.

What is the greatest product of four adjacent numbers in the
same direction (up, down, left, right, or diagonally) in the
20*20 grid?
'''
import numpy as np

a1 = [8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8]
a2 = [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0]
a3 = [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65]
a4 = [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91]
a5 = [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80]
a6 = [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50]
a7 = [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70]
a8 = [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21]
a9 = [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72]
a10 = [21, 36, 23, 9, 75,00, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95]
a11 = [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92]
a12 = [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57]
a13 = [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58]
a14 = [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40]
a15 = [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66]
a16 = [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69]
a17 = [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36]
a18 = [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16]
a19 = [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54]
a20 = [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 0, 89, 19, 67, 48]
a = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20]
a = np.array(a)


def solution(x):
    lenProduct = 4

    cols = x.shape[0]
    rows = x.shape[1]

    greatestProduct = 0
    greatestFactors = []

    # Checks each row
    for q in x:
        for i in range(rows - lenProduct+1):
            tempProduct = 1
            subNum = q[i:i+lenProduct]
            # print(subNum)
            for num in subNum:
                tempProduct *= num

            if tempProduct > greatestProduct:
                greatestFactors = subNum
                greatestProduct = tempProduct

    # Transpose
    b = np.copy(x)
    b = b.T

    # Checks each row of transposed matrix (thus columns)
    for q in b:
        for i in range(cols - lenProduct+1):
            tempProduct = 1
            subNum = q[i:i+lenProduct]
            # print(subNum)
            for num in subNum:
                tempProduct *= num

            if tempProduct > greatestProduct:
                greatestFactors = subNum
                greatestProduct = tempProduct

        
    xStep = 0
    yStep = 0

    # Diagonal from top left to bottom right
    while xStep <= rows - lenProduct:
        while yStep <= cols - lenProduct:
            print(x[yStep][xStep], x[yStep+1][xStep+1], x[yStep+2][xStep+2], x[yStep+3][xStep+3])
            vals = [x[yStep][xStep], x[yStep+1][xStep+1], x[yStep+2][xStep+2], x[yStep+3][xStep+3]]
            
            if np.prod(vals) > greatestProduct:
                greatestProduct = np.prod(vals)
                greatestFactors = vals

            yStep += 1
        yStep = 0
        xStep += 1

    b = np.copy(x)
    b = np.flip(b, axis=0)

    xStep = 0
    yStep = 0

    while xStep <= rows - lenProduct:
        while yStep <= cols - lenProduct:
            print(b[yStep][xStep], b[yStep+1][xStep+1], b[yStep+2][xStep+2], b[yStep+3][xStep+3])
            vals = [b[yStep][xStep], b[yStep+1][xStep+1], b[yStep+2][xStep+2], b[yStep+3][xStep+3]]
            
            if np.prod(vals) > greatestProduct:
                greatestProduct = np.prod(vals)
                greatestFactors = vals

            yStep += 1
        yStep = 0
        xStep += 1            

    print(greatestProduct)
    print(greatestFactors)

# Diagonal left->right
#  9 9 9 9
b1 = [1, 9, 2, 2, 1]
b2 = [1, 1, 9, 1, 1]
b3 = [1, 4, 1, 9, 1]
b4 = [1, 1, 1, 1, 9]
b5 = [1, 3, 3, 3, 1]
b = [b1, b2, b3, b4, b5]

b = np.array(b)

# solution(b)

# Diagonal right->left
# 20 9 9 9 
c1 = [1, 9, 2, 9, 1]
c2 = [1, 1, 9, 1, 1]
c3 = [1, 9, 1, 9, 1]
c4 = [20, 1, 1, 1, 9]
c5 = [1, 3, 3, 3, 1]
c = [c1, c2, c3, c4, c5]

c = np.array(c)

# solution(c)

# Left->right
#  11 19 12 19
d1 = [11, 19, 12, 19, 1]
d2 = [1, 1, 9, 1, 1]
d3 = [1, 9, 1, 9, 1]
d4 = [0, 1, 1, 1, 9]
d5 = [1, 3, 3, 3, 1]
d = [d1, d2, d3, d4, d5]

d = np.array(d)

# solution(d)


# Up->down
# 15 12 20 199
e1 = [11, 9, 12, 19, 1]
e2 = [15, 1, 9, 1, 1]
e3 = [12, 9, 1, 9, 1]
e4 = [20, 1, 1, 1, 9]
e5 = [199, 3, 3, 3, 1]
e = [e1, e2, e3, e4, e5]

e = np.array(e)

# solution(e)

solution(a)
