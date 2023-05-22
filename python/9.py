'''
A Pythagorean triplet is a set of three natural numbers,
    a < b < c,
for which,
    a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which,
    a + b + c = 1000.

Find the product abc.
'''

target = 1000

triplets = []

for i in range(int(target/2)+1, 1, -1):
    for j in range(int(target/2)+1, 1, -1):
        for k in range(int(target/2)+1, 1, -1):
            if i + j + k == target:
                triplets.append( (i, j, k) )

print(triplets)

for xs in triplets:
    i, j, k = xs
    if i**2 + j**2 == k**2:
        print(xs)
        print(i * j * k)
    
