'''
If the numbers 1 to 5 are written out in words: 
            one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were
written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 
342 (three hundred and forty-two) contains 23 letters and 
115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in 
compliance with British usage.

    {
        Damn Brits lmao
}

This solution can also be done by simply having an array of
the word lengths already computed:

    total += ones[i]            ...essentially...

I did it the way I did because I am intimidated by having to count
the lengths myself. Writing a program for me to do it would require
making this anyways. Why not just make the computer do all of it for me?

You might notice that some of the arrays contain placeholders.
This is because arrays are typically 0-indexed. When done this way
all we need to do is index it by the digit itself.
'''

ones = ['', 'one', 'two', 'three', 'four', 'five', 'six',
        'seven', 'eight', 'nine']
tens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
        'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
doubleAbove = ['','', 'twenty', 'thirty', 'forty', 'fifty',
               'sixty', 'seventy', 'eighty', 'ninety']
misc = ['and', 'hundred', 'thousand']


def singleDigit(numString):
    index = int(numString)

    if index == 0:
        return 0 

    print('X:    ', ones[index])

    return len(ones[index])


def doubleDigits(numString):
    global hundred
    finalString = ''
    i0, i1 = int(numString[0]), int(numString[1])

    if i0 == 0:
        return singleDigit(numString[1:])
    elif i0 == 1:
        print('1X:   ', tens[i1])
        return len(tens[i1])
    
    else:
        '''            X0                X'''
        finalString += doubleAbove[i0] + ones[i1]
        print('XX:   ', finalString)
        return len(finalString)
    

def tripleDigits(numString):
    finalString = ''
    i0 = int(numString[0])

    reducedNum = numString[1:]

    if i0 == 0:
        return doubleDigits(reducedNum)        
    
    followingDigitsLen = doubleDigits(reducedNum)


    '''            X00      hundred   '''
    finalString += ones[i0] + misc[1]

    if followingDigitsLen != 0:
        finalString += misc[0]   #''' and '''
        length = len(finalString)
        print('X00:  ', finalString)
        return length + followingDigitsLen

    print('X00:  ', finalString)
    return len(finalString)



def convertToWords(x):
    numString = str(x)
    numDigits = len(numString)

    if numDigits == 1:
        return singleDigit(numString)
    elif numDigits == 2:
        return doubleDigits(numString)
    elif numDigits == 3:
        return tripleDigits(numString)
    elif numDigits == 4:
        return len('onethousand')



solution = convertToWords(4)
print('\nsolution', solution)

solution = convertToWords(342)
print('\nsolution', solution)

solution = convertToWords(115)
print('\nsolution', solution)

solution = 0
for i in range(1,1001):
    solution += convertToWords(i)
    print('solution {}\n\n'.format(solution))