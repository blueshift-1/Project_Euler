__author__ = 'zwilson'

import math
import time
start_time = time.time()

def is_prime(n):

    prime = True

    if n == 2:
        prime = True
    elif n % 2 == 0:
        prime = False
    elif n == 1 or n == -1:
        prime = False
    elif n < 0:
        prime = False

    if prime == True:
        size = int(math.sqrt(n))/2
        for i in range(0,size):
            if n % (3 + 2 * i) == 0:
                return False
    return prime

total = 0
max_count = 0
primes = [2]
start = 0
i = 3

while(i < 5000000):

    if is_prime(i):
        primes.append(i)
    i += 2

i = 1

for i in range(0, len(primes)):

    local_total = 0

    j = 0
    while (local_total + primes[i+j] < 1000000):
        local_total += primes[i+j]
        j += 1

        if j > max_count and is_prime(local_total):
            max_count = j
            total = local_total

print(is_prime(total))

print("Total: " + str(total))
print("Start: " + str(max_count))
print("Run Time: %s seconds" % (time.time() - start_time))