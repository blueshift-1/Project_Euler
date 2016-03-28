__author__ = 'zwilson'


def itemized_factorial(num):
    num_str = str(num)
    total = 0

    for i in range(0,len(num_str)):
        total = total + factorial(int(num_str[i]))

    if total == num:
        return True
    return False

def factorial(num):
    product = 1
    for i in range(2,num+1):
        product *= i
    return product


total = 0
last_factorial = 2
for i in range(3,10000000):
    if itemized_factorial(i) ==  True:
        total += i
        last_factorial = i

print ("Total: " + str(total))
print ("Last Factorial: " + str(last_factorial))