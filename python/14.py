'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

def evenStep(x):
    return int(x/2)

def oddStep(x):
    return int(3 * x + 1)

''' 
    Please return to this when you begin your second pass.
    I whole heartedly believe there is a way to implement memoization
    with this method. I just do not have the capability to do so right now.
'''
def failedSolution():
    n = 0           # This is our tracking number
    m = 1           # This is our starting number
    # m = 500
    # quickStopNum = 500000
    quickStopNum = 999999

    maxStart = 0
    maxSteps = 0

    stepCounts = {1:1}


    while m < quickStopNum:
        print('\n\n\n\n\n\n\n\n\n')
        n = m
        numSteps = 1

        while(n > 1):
            if n not in stepCounts:
                numSteps += 1
            
                print(n)
            
                if n % 2 == 0:
                    n = evenStep(n)
                else:
                    n = oddStep(n)
            else:
                numSteps += stepCounts[n]
                break
        


        if numSteps > maxSteps:
            maxSteps = numSteps
            maxStart = n
        
        m -= 1




'''
    From: https://stackoverflow.com/questions/29196251/longest-collatz-sequence-efficiency
    By: Aristide on stackoverflow

    Good place to talk about memoization and what that is all about.
'''
def counts(n):
    if n not in stepCounts:
        if n % 2 == 0:
            stepCounts[n] = 1 + counts(evenStep(n))
        else:
            stepCounts[n] = 1 + counts(oddStep(n))

    return stepCounts[n]

stepCounts = {1: 1}

maxStart = 0
maxSteps = 0

for start in range(1, 1000000):
    steps = counts(start)

    if steps > maxSteps:
        maxSteps = steps
        maxStart = start
        print('Max Start: {}\nMax Steps:{}\n'.format(maxStart, maxSteps))

    

print("\nSolution:")
print("=========")
print('Max Start: {}\nMax Steps:{}\n'.format(maxStart, maxSteps))
