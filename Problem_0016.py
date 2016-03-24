__author__ = 'zwilson'

value = 2**1000
print value
value = str(value)

total = 0
for i in range(0,len(value)):
    total += int(value[i])

print(total)