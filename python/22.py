'''
Using names.txt (right click and 'Save Link/Target As...'),
a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. 

Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list 
to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, 
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
'''

with open('p022_names.txt') as f:
    line = f.read()

print(line)
print(type(line))
print(len(line))

withoutCommas = line.split(',')
print(withoutCommas)

names = []

for name in withoutCommas:
    names.append( name.replace('"', '') )



solution = 0

names.sort()

print(names)

position = 1
for name in names:
    nameScore = 0
    for char in name:
        nameScore += (ord(char) - 64)
    

    solution += nameScore * position
    position += 1


print(solution)
