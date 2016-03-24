__author__ = 'zwilson'

def number_word_generator(num):
    num_string = str(num)

    output_string = ""

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

for i in range(990,1001):
    word = number_word_generator(i)
    print(word+": "+str(count_alpha(word)))

