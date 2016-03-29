__author__ = 'zwilson'

import time
start_time = time.time()

def triangle_number(n):
    return int(0.5 * n * (n + 1))

def pentagonal_number(n):
    return int(0.5 * n * (3 * n - 1))

def hexagonal_number(n):
    return int(n * (2 * n - 1))


start_rng = 286
end_rng = 100000

tri = []
pent = []
hex = []

for i in range(start_rng, end_rng):
    tri.append(triangle_number(i))
    pent.append(pentagonal_number(i))
    hex.append(hexagonal_number(i))

size = len(tri)
for i in range(0, size):
    val = tri[i]
    if val in pent and val in hex:
        print("Triple Number: " + str(val))
        break

print("Run Time: %s seconds" % (time.time()-start_time))





