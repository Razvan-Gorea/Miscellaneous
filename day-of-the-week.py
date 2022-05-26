#!/usr/bin/env python3

#1-7 Starting with Monday, ending on Sunday

month_num = int(input("Give me the month number: ")) - 1

day_num = int(input("Give me the day number: ")) - 1

day_of_year = ((month_num * 30) + day_num) 

day_of_week = (day_of_year % 7) + 1

print(day_of_week)