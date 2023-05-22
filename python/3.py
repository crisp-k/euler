'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
'''

import math

start = 600851475143
# start = 6008514751

primes, primeFactors = [], []

def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    
    return True

for x in range(2, int(math.sqrt(start))):
    if x % 2 == 0:
        continue
    elif isPrime(x):
        primes.append(x)

print(primes)

for val in primes:
    if start % val == 0:
        primeFactors.append(val)

print(primeFactors)