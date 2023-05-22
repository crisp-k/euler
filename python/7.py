'''
By listing the first six prime numbers:
2, 3, 5, 7, 11, and 13, we can see that 
the 6th prime is 13.

What is the 10 001st prime number?
'''

def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
        
    return True

def generatePrimes(end):
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


targetPrime = 10001
primes = generatePrimes(targetPrime)

print(primes[-1])
