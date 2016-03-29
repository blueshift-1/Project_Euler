__author__ = 'zwilson'

import time

start_time = time.time()

def number_word_generator(num):
    num_string = str(num)
    special = {1000: "One Thousand", 900: "Nine Hundred", 800: "Eight Hundred",
               700: "Seven Hundred", 600: "Six Hundred", 500: "Five Hundred",
               400: "Four Hundred", 300: "Three Hundred", 200: "Two Hundred",
               100: "One Hundred"}
    output_string = ""


    if num in special.keys():
        return special[num]
    else:
        for i in range(0,len(num_string)):
            place = len(num_string)-1-i

            value = get_number_name(num_string[place],i,"")

            if value == "SPECIAL TENS":
                output_string = get_number_name(num_string[place+1],0,"SPECIAL TENS")

            else:
                output_string = value + " " + output_string

    return output_string

def get_number_name(num,place,special):

    ones = ["","one","two","three","four","five","six","seven","eight","nine"]
    tens = ["","SPECIAL CASE","twenty-","thirty-","forty-","fifty-","sixty-","seventy-","eighty-","ninety-"]
    special_tens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]

    if special == "SPECIAL TENS":
        return special_tens[int(num)]
    elif place == 0:
        return ones[int(num)]
    elif place == 1:
        if num == "1":
            return "SPECIAL TENS"
        else:
            return tens[int(num)]
    elif place == 2:
        return ones[int(num)] + " " + "hundred and"
    elif place == 1:
        return ones[int(num)] + " thousand"

def count_alpha(string):
    alpha_count = 0
    for i in range(0,len(string)):
        if str.isalpha(string[i]):
            alpha_count+=1
    return alpha_count

word = ""
for i in range(1,1001):
    word += number_word_generator(i)

character_count = 0
for i in range(0,len(word)):
    if word[i].isalpha() == True:
        character_count += 1

print ("Character Count: " + str(character_count))
print("Run Time: %s seconds" % (time.time() - start_time))