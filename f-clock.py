import datetime
import random


ONES_DICT = [
    '', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'
]

TEENS = [
    'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen',
    'Seventeen', 'Eighteen', 'Nineteen'
]

TENS_DICT = [
    '', '', 'Twenty', 'Thirty', 'Fourty', 'Fifty', 'Sixty', 'Seventy',
    'Eighty', 'Ninety'
]


def n2a(number):
    if number == 0:
        return 'zero'
    elif number < 10:
        return ONES_DICT[number % 10]
    elif number < 20 and number > 9:
        return TEENS[number - 10]
    elif number % 10 == 0:
        return TENS_DICT[number // 10]
    else:
        return TENS_DICT[number // 10] + ' ' + ONES_DICT[number % 10]


def next(n):
    return 12 if n == 11 else n + 1


def fuzzyTime(hour, minutes):
    cond = ((minutes + 2) % 60) // 5
    if minutes > 33:
        hour = next(hour)
    if hour != 12:
        hour = hour % 12
    if cond == 0:
        return n2a(hour) + ' o\'clock'

    elif cond == 3:
        return 'Quarter' + ' past ' + n2a(hour)
    elif cond == 6:
        return 'Half' + ' past ' + n2a(hour)
    elif cond == 9:
        return 'Quarter' + ' to ' + n2a(hour)
    elif 0 < cond < 6:
        return n2a(cond * 5) + ' past ' + n2a(hour)
    else:
        return n2a(60 - cond * 5) + ' to ' + n2a(hour)


# Get fuzzy clock
time = datetime.datetime.now().timetuple()
hour = time[3]
minutes = time[4]
print(fuzzyTime(hour, minutes))
