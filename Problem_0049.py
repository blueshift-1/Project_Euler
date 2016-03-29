from itertools import permutations
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



for i in range(0,9):
    for j in range(j,9):
        for k in range(k,9):
            for l in range(l,9):
                seq = [i,j,k,l]




print("Run Time: %s seconds" % (time.time() - start_time))