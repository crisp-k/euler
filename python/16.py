'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

def testIntLen():
    x = 1

    for i in range(999999):
        x *= 100000000000000
        print(x)

    
def solution(exponent):
    solution = 0
    
    x = 2 ** exponent
    y = str(x)
    
    for char in y:
        solution += int(char)

    print('x value:  ', x)
    print('solution: ', solution)


solution(1000)