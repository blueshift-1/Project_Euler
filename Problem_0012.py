__author__ = 'zwilson'

def factor(num):

    factors = []
    for i in range(1,int(num/2)+1):
        if num % i == 0:
            factors.append(i)
    if num!=0 and num!=1:
        factors.append(num)

    return factors


exit = False
i = 1
triangle_number = 0

while(exit==False):
    triangle_number += i

    if len(factor(triangle_number))>500:
        exit = True
        print(i)
        print(triangle_number)


    i += 1

