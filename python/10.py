'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
from commonMethods import *

target = 2000000

primes = generatePrimesUpTo(target)

print(primes)
print("solution: ", sum(primes))


