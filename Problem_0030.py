__author__ = 'zwilson'

def validate_power_equivalence(n,pow):
    n_str = str(n)

    sum = 0
    for i in range(0,len(n_str)):
        sum = sum + int(n_str[i]) ** pow

    if sum == n: return True
    return False

count = 0
sum = 0
for i in range(2,1000000):
    if validate_power_equivalence(i,5) == True:
        print(i)
        count += 1
        sum += i

print("*********************")
print("Count: " + str(count))
print("Sum:   " + str(sum))