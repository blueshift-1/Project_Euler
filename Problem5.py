__author__ = 'zwilson'

def isDivisible(num,min,max):
    valid = True

    for i in range(min,max):
        if (num % i)!=0:
            valid = False

    return valid

i=1
exit = False
max = 20

while exit==False:

    if isDivisible(i*max,1,max) == True:
        print(i*max)
        exit = True
    i+=1



