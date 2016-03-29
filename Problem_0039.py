import time
start_time = time.time()

max_solutions = 0
max_solutions_perimeter = 0

for p in range(10,1001):

    local_solutions = 0
    for a in range(1, int(p/2)):
        for b in range(a, int(p/2)):
            if a + b < p:
                c = p - a - b
                if a ** 2 + b ** 2 == c ** 2:
                    local_solutions += 1


                    if local_solutions > max_solutions:
                        max_solutions = local_solutions
                        max_solutions_perimeter = p
print (max_solutions)
print(max_solutions_perimeter)
print("Run Time: %s seconds" % (time.time() - start_time))