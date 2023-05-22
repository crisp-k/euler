'''
By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click 
and 'Save Link/Target As...'), a 15K text file containing a triangle 
with one-hundred rows.
'''
from commonMethods import *

test = '06'
testInt = int(test)

print(test)


with open('p067_triangle.txt') as f:
    fullTriangle = []
    
    for line in f:
        fullTriangle.append([int(x) for x in line.split()])


print(len(fullTriangle))
for i in range(10):
    print(fullTriangle[i])


solveTrianglePath(fullTriangle)