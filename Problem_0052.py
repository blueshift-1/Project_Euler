__author__ = 'zwilson'

import time
start_time = time.time()

def validateDigits(list):

    master = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

    for i in range(0, len(list[0])):
        master[int(list[0][i])] += 1
    for i in range (1, len(list)):
        local = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

        for j in range(0, len(list[i])):
            local[int(list[i][j])] += 1

        if local != master:
            return False

    return True

for i in range(100000,200000):

    vals = []
    for j in range(1,7):
        vals.append(str(i * j))
    if validateDigits(vals) == True:
        print(i)

print("Run Time: %s seconds" % (time.time() - start_time))
