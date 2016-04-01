__author__ = 'zwilson'

import time
start_time = time.time()

class Poker_Hand:

    ranking = 0
    high_card = 0
    hand_score = 0
    values = []
    suits = []

    def set_hand(self, hand):
        card_value = {"2":0,"3":1,"4":2,"5":3,"6":4,"7":5,"8":6,"9":7,"T":8,"J":9,"Q":10,"K":11,"A":12}
        for card in hand:
            self.values.append(card_value[card[0]])
            self.suits.append(card[1])

        self.values.sort()
        self.suits.sort()
        self.high_card = max(self.values)
        self.hand_score = sum(self.values)

    def calc_hand_score(self):
        is_flush = self.flush()
        is_straight = self.straight()
        max_of_a_kind = self.of_a_kind()

        if is_flush and is_straight and self.high_card == 12:
            return 9
        elif is_flush and is_straight:
            return 8
        elif max_of_a_kind == 4:
            return 7
        elif is_flush:
            return 5
        elif is_straight:
            return 4
        elif max_of_a_kind == 3:
            return 3
        else: return 0

    def flush(self):

        master = self.suits[0]
        for suit in range(1,len(self.suits)):
            if self.suits[suit] != master:
                return False
        return True

    def straight(self):

        initial = self.values[0]
        for i in range(1,len(self.values)):
            if self.values[i] == initial + 1:
                initial += 1
            else:
                return False

        return True

    def of_a_kind(self):

        current_card = self.values[0]
        max_count = 1
        count = 1

        for i in range(1,len(self.values)):
            if current_card == self.values[i]:
                count += 1
                if count > max_count:
                    max_count = count
            else:
                count = 0

        return max_count

    def two_pair(self):
        return True





    def compare(self,other_hand):

        if self.ranking > other_hand.ranking:
            return 1
        if self.ranking < other_hand.ranking:
            return -1
        else:
            return 0


def import_file(file_name):
    output = []
    with open(file_name) as inputfile:
        for line in inputfile:
            output.append(line.strip().split(" "))
    return output


def compare_hands(hand_1, hand_2):


    return 1

data = import_file("p054_poker.txt")
results = [0,0]

for pair in range(0,int(len(data)/2)):
    winner = compare_hands(data[2*pair],data[2*pair+1])

    results[winner] += 1

print("Run Time: %s seconds" % (time.time()-start_time))