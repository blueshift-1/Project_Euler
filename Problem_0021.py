import time

def divisors(num):

    list = [1]
    if num % 2 == 0:
        list.append(2)
        for i in range(3,int(num/2)+1):
            if num % i == 0:
                list.append(i)
    else:
        for i in range(1, int(num/4)):
            if num % (1+i*2):
                list.append(1+i*2)

    return list

start_time = time.time()

dict = {}
for i in range(1,10000):
    j = sum(divisors(i))
    k = sum(divisors(j))

    if i == k and i != j:
        dict[i] = True
        dict[j] = True

total = 0
for key in dict.keys():
    total += key
    print(key)

print("Total: " + str(total))

print("Run Time: %s seconds" % (time.time() - start_time))