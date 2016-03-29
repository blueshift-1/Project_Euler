import time
import random
start_time = time.time()

def generate_triangle():
    output =    [[75],
                [95, 64],
                [17, 47, 82],
                [18, 35, 87, 10],
                [20,  4, 82, 47, 65],
                [19,  1, 23, 75,  3, 34],
                [88,  2, 77, 73,  7, 63, 67],
                [99, 65,  4, 28,  6, 16, 70, 92],
                [41, 41, 26, 56, 83, 40, 80, 70, 33],
                [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
                [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
                [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
                [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
                [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
                [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]]
    return output
def monte_carlo(a, b):
    total = a + b
    if random.random() < a/total:
        return (0, a)
    else:
        return (1, b)

best_total = 0
index = 0

triangle = generate_triangle()

for i in range (1,1000):
    index = 0
    local_total = triangle[0][index]
    for i in range(1,len(triangle)):
        val = monte_carlo(triangle[i][index],triangle[i][index + 1])
        index += val[0]
        local_total += val[1]

    if local_total > best_total:
        best_total = local_total

print(best_total)
print("Run Time: %s seconds" % (time.time() - start_time))