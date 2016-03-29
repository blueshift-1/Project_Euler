__author__ = 'zwilson'

import time
start_time = time.time()

def series(n):
    return n ** n

summation = 0
for i in range(1,1000):
    val = series(i) % 10000000000
    summation += val

    summation %= 10000000000



print(summation)
print("Run Time: %s seconds" % (time.time()-start_time))