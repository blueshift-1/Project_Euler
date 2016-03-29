__author__ = 'zwilson'

import time
from itertools import permutations

start_time = time.time()

rules = {(2,3,4):2,(3,4,5):3,(4,5,6):5,(5,6,7):7,(6,7,8):11,(7,8,9):13,(8,9,10):17}
num = [0,1,2,3,4,5,6,7,8,9]

def check_rules(rules, num_str):

    for key in rules.keys():
        digits = ""
        for i in range(0, len(key)):
            digits += num_str[key[i]-1]

        if int(digits) % rules[key] != 0:
            return False

    return True

total = 0
for perm in permutations(num):
    val = ""
    for n in perm:
        val += str(n)
    if check_rules(rules,val):
        total += int(val)

print("Total Sum: " + str(total))
print("Run Time: %s seconds" % (time.time()-start_time))