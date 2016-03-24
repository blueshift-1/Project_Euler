__author__ = 'zwilson'

import math

global coeff_a
global coeff_b

def special_quadratic(a,b,n):
    return n * n + a * n + b

def is_prime(n):

    prime = True

    if n % 2 == 0:
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

def max(val_1, val_2, a, b):
    if val_1 < val_2:
        global coeff_a
        coeff_a = a
        global coeff_b
        coeff_b = b
        return val_2
    return val_1

output = 0


for i in range(-1000,1001):
    for j in range(-1000,1001):
        n = 0

        if i == -79 and j == 1601:
            print(str(i)+","+str(j)+","+str(n)+str(special_quadratic(i,j,n)))

        while is_prime(special_quadratic(i,j,n)) == True:
            if i == -79 and j == 1601:
                print(n)
            n += 1
            output = max(output, n, i, j)

print(output)
print(coeff_a)
print(coeff_b)
print(coeff_a*coeff_b)