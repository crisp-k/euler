'''
2520 is the smallest number that can be divided by each of
the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
'''

import numpy as np


def possibleSolution():
    
    def divisible(num, x):
        digits = range(2, x+1)

        for digit in digits:
            if num % digit != 0:
                return False

        return True

   
    num = 2000

    run = True

    while(run):
        if num % 2 != 0:
            num += 1
            continue

        if divisible(num, 5):
            if divisible(num, 10):
                if divisible(num, 15):
                    if divisible(num, 20):
                        print('solution: ', num)
                        break
                    else:
                        print('fluke: ', num)
                        num += 1
                else:
                    num += 1
                    continue
            else:
                num += 1
                continue
        else:
            num += 1
            continue
    print(num)

possibleSolution()


def solution():
    
    def isPrime(x):
        for i in range(2, x+1):
            if x % i == 0:
                return False
        return True
                
    primes = []
    
    for i in range(2, 200):
        if i % 2 == 0:
            continue
        if isPrime(i):
            primes.append(i)
    
    print(primes)

    
# solution()