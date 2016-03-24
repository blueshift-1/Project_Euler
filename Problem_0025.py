__author__ = 'zwilson'

def fibonnaci_loop(n):

    previous = 0
    current = 1
    i = 1

    while len(str(current)) < n:

        temp = current
        current = previous + current
        previous = temp
        i = i + 1
    return i

print(fibonnaci_loop(1000))