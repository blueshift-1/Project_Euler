__author__ = 'zwilson'

import math
import time

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


def truncatable_primes(num):
    num_str = str(num)
    num_str_left = str(num)
    num_str_right = str(num)

    if is_prime(num) == False:
        return False

    for i in range(0, 2*(len(num_str)-1)):
        if i < len(num_str)-1:

            num_str_left= num_str_left[:len(num_str_left)-1]
            if not is_prime(int(num_str_left)):
                return False
        else:

            num_str_right = num_str_right[1:]
            if not is_prime(int(num_str_right)):
                return False
    return True

start_time = time.time()
total = 0
count = 0
i = 10

while count < 11:
    if truncatable_primes(i) == True:
        print(i)
        count += 1
        total += i
    i += 1



print("Count: " + str(count))
print("Sum:   " + str(total))

print("Run Time: %s seconds" % (time.time()-start_time))