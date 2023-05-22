
import numpy as np

def isPrime(x):
    for i in range(2, int(np.sqrt(x) + 1)):
        if x % i == 0:
            return False
        
    return True

def generateNPrimes(end):
    primes = []
    num = 0

    while len(primes) < end:
        if num != 2 and num % 2 == 0:
            num += 1
            continue

        if isPrime(num):
            primes.append(num)
            num += 2
        else:
            num += 1

    return primes

def generatePrimesUpTo(val):
    primes = [] 
    
    for i in range(2, val):
        # if i != 2 and i % 2 == 0:
            # continue
        if isPrime(i):
            print(i)
            primes.append(i)


    return primes




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


def solveTrianglePath(tri):
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


def findDivisors(n):
    divisors = []

    for i in range(1, int(n/2 + 1)):
        if n % i == 0:
            divisors.append(i)    

    return divisors