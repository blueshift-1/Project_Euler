import time
start_time = time.time()
def lattice(height, width):
    return choose(height + width, min([height,width]))

def choose (n, k):
    return factorial(n)/(factorial(k) * factorial(n - k))


def factorial (n):
    output = 1
    for i in range(2,n+1):
        output *= i
    return output

width = 20
height = 20

print("Lattice of " + str(width) + "x" + str(height) + ": " + str(lattice(height,width)))
print("Run Time: %s seconds" % (time.time() - start_time))