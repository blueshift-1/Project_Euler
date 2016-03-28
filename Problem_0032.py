__author__ = 'zwilson'

def search_pandigital(ls,num):

    output = False
    num_str = str(num)


    for i in range(0,len(ls)):
        dict = { 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

        combined_str = num_str + str(ls[i][0]) + str(ls[i][1])
        if len(combined_str) == 9:

            for j in range(0,len(combined_str)):
                if combined_str[j] != "0":
                    dict[int(combined_str[j])] += 1
            #print(str(ls[i][0]) + "," + str(ls[i][1]) + ": " + str(dict))
            if _validate_pandigital(dict) == True:
                output = True

    return output


def _validate_pandigital(d):
    for key, val in d.items():
        if val != 1:
            return False
    return True


def factor_pairs(n):
    ls = []
    rng = range(1,int(n/2))
    for i in rng:
        if n % i == 0:
            ls.append((i,n/i))
    return ls

total = 0

for num in range(1, 10000):
    pairs = factor_pairs(num)

    if search_pandigital(pairs,num) == True:
        total+=num

print(total)