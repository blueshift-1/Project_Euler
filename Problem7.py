__author__ = 'zwilson'

def isPrime(num):
    valid = True

    # Handles some basic conditions that expel items
    num_str = str(num)

    if num_str[len(num_str)-1]==5:
        valid = False
    if num_str[len(num_str)-1]==0:
        valid = False
    if num ==0:
        valid = False
    if num % 2 == 0:
        valid = False
    if num ==2:
        valid = True


    # Handles brute force search using odd numbers less thant 1/2 the item
    if valid == True:
        i = 3
        half_num = int(0.5 * num)
        while i < half_num:
            if num % i == 0:
                valid = False
                i = num
            i+= 2
    return valid



primes_found = 1
i = 1

while primes_found < 10001:
    i+=2
    if isPrime(i)==True:
        primes_found +=1



print(i)