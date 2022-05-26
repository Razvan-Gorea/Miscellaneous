#!/usr/bin/env python3

month_num = int(input("Give me the month number: "))
day_num = int(input("Give me the day number: "))
day_of_year = ((month_num - 1) * 30) + day_num
print(f'Day of year: {day_of_year}')