__author__ = 'zwilson'


min = 1
max = 100

squareOfSums = 0
for i in range(min,max+1):
    print(i)
    squareOfSums += i

print(squareOfSums)
squareOfSums = squareOfSums * squareOfSums



sumOfSquares = 0
for i in range(min,max+1):
    sumOfSquares += i * i
print(sumOfSquares)


print(squareOfSums - sumOfSquares)
