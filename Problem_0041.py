__author__ = 'zwilson'


from itertools import permutations
import time
import math

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


def generate_pandigitals(n):

    pan = []
    for i in range(1,n+1):
        pan.append(i)

    pan_prime = 0
    for perm in permutations(pan):
        pan = ""
        for i in range(0,len(perm)):
            pan += str(perm[i])

        if is_prime(int(pan)) == True:
            if int(pan) >  pan_prime:
                pan_prime = int(pan)

    return pan_prime


max_prime = 0
for i in range(2,9):
    val = generate_pandigitals(i)
    if val > max_prime:
        max_prime = val

print(max_prime)
print("Run Time: %s seconds" % (time.time()-start_time))