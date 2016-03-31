__author__ = 'zwilson'

import time
start_time = time.time()

def import_file(file_name):
    output = []
    with open(file_name) as inputfile:
        for line in inputfile:
            output.append(line.strip().split(" "))
    return output

def convert_hand(hand):
    for card in hand:


def compare_hands(hand_1, hand_2):


    return 1

data = import_file("p054_poker.txt")
results = [0,0]

for pair in range(0,int(len(data)/2)):
    winner = compare_hands(data[2*pair],data[2*pair+1])

    results[winner] += 1

print("Run Time: %s seconds" % (time.time()-start_time))