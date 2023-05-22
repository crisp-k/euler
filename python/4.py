'''
A palindromic number reads the same both ways. The largest
palindrome made from the product of two 2-digit numbers is:
9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

# testStr = 'test'

# test = 'abc'

# for char in test:
#     print(char)

# reverseTest = test[::-1]

# print(reverseTest)

# if test == reverseTest:
#     print(True)



def isPalindrome(x):
    val = str(x)

    if val == val[::-1]:
        return True
    
    return False

largest = 0

def solve4_2product():

    for i in range(99, 0, -1):
        for j in range(99, 0, -1):
            product = i * j

            if isPalindrome(product):
                print(product)
                return
            else:
                continue
            
solve4_2product()

def solve4():
    largest = 0

    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            product = i * j
            # print(i, j, product)

            if isPalindrome(product):
                if product > largest:
                    largest = product
            else:
                continue

    print(largest)
    return

solve4()