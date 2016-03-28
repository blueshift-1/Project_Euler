__author__ = 'zwilson'

def dec2binary(dec):

    bin = ""

    while (dec > 0):

        val = dec % 2
        bin = str(val) + bin

        if val == 1:
            dec -= 1

        dec /= 2

    return int(bin)

def is_palendrome(str):
    if str == _reverse(str):
        return True
    return False

def _reverse(str):
    reverse_str = ""
    length = len(str)-1

    for i in range(0,len(str)):
        reverse_str += str[length-i]

    return reverse_str

total = 0

for i in range(1,1000000):
    if is_palendrome(str(i)) == True and is_palendrome(str(dec2binary(i))) == True:
        total += i

print(total)