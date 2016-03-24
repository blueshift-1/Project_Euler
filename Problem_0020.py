__author__ = 'zwilson'

def factorial(n):
    f = 1
    for i in range(1,n+1):
        f *= i
    return f

val = factorial(100)
val = str(val)

summation = 0
for i in range(0,len(val)):
    summation += int(val[i])

print(summation)