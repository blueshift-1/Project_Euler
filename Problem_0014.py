__author__ = 'zwilson'

def collatz_sequence(n):
    if n%2==0:
        return n/2
    else:
        return 3 * n + 1

def collatz_chain(n):
    i = 1
    while n!=1 or i < 10000000:
        n = collatz_sequence(n)
        i = i + 1

    return i

def max(val_1,val_2):
    if val_1 > val_2:
        return val_1
    return val_2

max_chain = 0
for i in range(1,1000000):
    max(max_chain,collatz_chain(i))

print(max_chain)