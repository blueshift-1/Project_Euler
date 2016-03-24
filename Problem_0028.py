__author__ = 'zwilson'

def spiral_diagonal(width):
    sum = 1
    current = 1

    for i in range(0,int((width-1)/2)):
        for j in range(0,4):
            current = current + 2 * (i + 1)
            sum+= current

    return sum

length = 1001
print(spiral_diagonal(length))

