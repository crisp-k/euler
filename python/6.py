'''
The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 3025

Hence the difference between the sum of the squares of the
first ten natural numbers and the square of the sum is,
    3025 - 385 = 2640

Find the difference between the sum of the squares of the 
first one hundred natural numbers and the square of the sum.
'''

def sumOfSquares(start, end):
    result = 0

    nums = range(start, end+1)
    
    for num in nums:
        result += num * num

    return result

def squareOfSums(start, end):
    nums = range(start, end+1)

    result = sum(nums)

    result *= result

    return result

endPoint = 100

x1 = sumOfSquares(1, endPoint)
x2 = squareOfSums(1, endPoint)

if x2 > x1:
    print(x2 - x1)
else:
    print(x1 - x2)


