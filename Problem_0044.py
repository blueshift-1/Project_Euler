__author__ = 'zwilson'

import time
start_time = time.time()

def pentagonal_number(n):
    return int(n * (3 * n - 1) * 0.5)


pent = []
for i in range(1000, 10000):
    pent.append(pentagonal_number(i))

for j in range(1, len(pent)):
    for k in range(j+1, len(pent)):
        pent_sum = pent[j] + pent[k]
        pent_diff = abs(pent[k] - pent[j])

        #print("(" + str(j) + "," + str(k) + ") Sum: " + str(pent_sum) + " | Diff: " + str(pent_diff))
        if pent_sum in pent and pent_diff in pent:
            print("Pentagonal Difference: " + str(pent_diff))
            print("(" + str(j) + "," + str(k) + ")")
            break

print("Run Time: %s seconds" % (time.time()-start_time))