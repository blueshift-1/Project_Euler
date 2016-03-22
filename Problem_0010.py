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

# Assumes 2 and uses odd rule for primes for the rest
sum_of_primes = 2
i = 3

while (i<2000000):

    if isPrime(i):
        sum_of_primes += i
        print(i)
    i+=2
print("------ Sum of Primes ------")
print(sum_of_primes)