__author__ = 'zwilson'

def isPythagoreanTriplet (a,b,c):
    if a*a + b*b == c*c:
        return True
    else:
        return False


sum = 1000

for i in range(1,sum-1):
    for j in range(i+1,sum):
        k = sum - j - i
        if isPythagoreanTriplet(i,j,k)== True:
            print (i*j*k)
