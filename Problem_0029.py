__author__ = 'zwilson'


def exponential (a,b):
    return a ** b

a = range(2,101)
b = range(2,101)
dict = {}

for i in a:
    for j in b:
        dict[exponential(i,j)] = True

print (len(dict))

