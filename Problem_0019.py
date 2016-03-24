__author__ = 'zwilson'


def days_in_month(year, month):
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        return 31
    elif month==4 or month==6 or month==9 or month==11:
        return 30
    else:
        if year % 4 != 0:
            return 28
        elif year % 100 != 0:
            return 29
        elif year % 400 != 0:
            return 28
        else:
            return 29



year = 1900
day = 6
month = 1
month_days = days_in_month(year,month)
sunday_the_first = 0

while year < 2000:

    if day > month_days:

        day = day - month_days
        month = (month + 1) % 13


        if month == 0:
            year += 1
            month = 1

        month_days = days_in_month(year,month)



    if day == 1:

        sunday_the_first += 1


    day += 7



print(sunday_the_first)

