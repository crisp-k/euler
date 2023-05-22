'''
You are given the following information, but you may prefer 
to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, 
but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during 
the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''
days = ['', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
months = [0, 31, 28, 31, 31, 30, 31, 31, 31, 30, 31, 30, 31]
monthNames = ['', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'november', 'october', 'december']

day = 2
sundays = 0

for year in range(1901, 2001):
    if year % 4 == 0 and year % 400 == 0:
        months[2] = 29
    elif year % 400 == 0:
        months[2] = 28

    for i in range(len(months)):
        print("\n\nMonth: ", monthNames[i])
        for j in range(months[i]):

            if days[day] == 'sunday' and j == 1:
                sundays += 1

            if day + 1 == 8:
                day = 1
            else:
                day += 1

print(sundays)


