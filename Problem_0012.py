__author__ = 'zwilson'

import math
import time
start_time = time.time()

# Source http://stackoverflow.com/questions/21783160/sieve-of-atkin-implementation-in-python
def sieveOfAtkin(limit):
    P = [2,3]
    sieve=[False]*(limit+1)
    for x in range(1,int(math.sqrt(limit))+1):
        for y in range(1,int(math.sqrt(limit))+1):
            n = 4*x**2 + y**2
            if n<=limit and (n%12==1 or n%12==5) : sieve[n] = not sieve[n]
            n = 3*x**2+y**2
            if n<= limit and n%12==7 : sieve[n] = not sieve[n]
            n = 3*x**2 - y**2
            if x>y and n<=limit and n%12==11 : sieve[n] = not sieve[n]
    for x in range(5,int(math.sqrt(limit))):
        if sieve[x]:
            for y in range(x**2,limit+1,x**2):
                sieve[y] = False
    for p in range(5,limit):
        if sieve[p] : P.append(p)
    return P

triangle = 0
index = 1

def prime_factorization(n):
    primes = sieveOfAtkin(int(n+1))
    prime_index = 0
    factors = {primes[prime_index]:0}

    while n > 1:
        if n % primes[prime_index] == 0:
            factors[primes[prime_index]] += 1
            n /= primes[prime_index]
        else:
            prime_index += 1
            factors[primes[prime_index]] = 0

    return factors

def factor_count(factorization):
    count = 1
    for freq in factorization.values():
        if freq > 0:
            count *= (freq + 1)
    return count

def triangle_number(current, next_index):
    return current + next_index

count = 0

# Jump start to first triangle number that is in the 500 divisors range

while (triangle < 72414400
):
    triangle  = triangle_number(triangle,index)
    index += 1

while(count < 500):
    triangle =  triangle_number(triangle,index)

    factorization = prime_factorization(triangle)
    count = factor_count(factorization)

    if count > 400:
        print ("400: " + str(triangle))
    elif count > 250:
        print ("250: " + str(triangle))
    index += 1

print "Triangle with over 500 divisors: " + str(triangle)

print("Run Time: %s seconds" % (time.time() - start_time))