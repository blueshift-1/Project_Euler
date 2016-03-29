import time

start_time = time.time()

def multiplicative_pandigital(num):
    pan_string = ""
    i = 1
    while len(pan_string) < 9:
        pan_string += str(i*num)
        i += 1

    if len(pan_string) > 9:
        return False
    else:
        dict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
        for i in range(0,len(pan_string)):
            if pan_string[i]  != '0':
                dict[int(pan_string[i])] += 1
        if _validate_pandigital(dict) == True:
            return pan_string
        else:
            return False

def _validate_pandigital(d):
    for key, val in d.items():
        if val != 1:
            return False
    return True

def max(val_1, val_2):
    if val_1 > val_2:
        return val_1
    return val_2

upper_range = 329218

max_pandigital = 0
for i in range(1,upper_range):
    val = multiplicative_pandigital(i)
    if val != False:
        max_pandigital = max(max_pandigital,int(val))

print ("Max Value: " + str(max_pandigital))

print("Run Time: %s seconds" % (time.time() - start_time))