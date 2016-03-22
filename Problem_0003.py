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

def getFactors(val, divisor):

    exit = False
    primeDivisor = -1
    dict = {}
    remainder = -1
    while (exit==False):

        remainder = val % divisor
        divisor += 1

        if remainder == 0 or divisor > int(val/2):
            exit = True

    if remainder == 0:
        divisor -= 1
        val = val/divisor

        primeDivisor = divisor
        dict = getFactors(val,divisor)
    else:
        primeDivisor = val

    dict[primeDivisor]=primeDivisor
    return dict


dict = (getFactors(600851475143 ,2))

max = 0
for k in dict.keys():
    if k > max:
        max = k

print max
print(isPrime(max))
