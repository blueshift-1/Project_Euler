

from itertools import permutations

a = [0,1,2,3,4,5,6,7,8,9]
i = 1
for item in permutations(a):
    if i == 1000000:
        print(item)
    i += 1
