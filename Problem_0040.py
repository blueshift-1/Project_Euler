import time
start_time = time.time()


def generate_champernowne(num_digits):
    champernowne = ""

    i = 1
    while(len(champernowne)<num_digits):
        champernowne += str(i)
        i += 1

    return champernowne

indexes = [1,10,100,1000,10000,100000,1000000]
series = generate_champernowne(max(indexes))

total = 1
for i in range(0, len(indexes)):
    total *= int(series[indexes[i]-1])

print(total)
print("Run Time: %s seconds" % (time.time() - start_time))