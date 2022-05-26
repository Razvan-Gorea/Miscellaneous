#!/usr/bin/env python3

x1 = int(input("Give the x1 coordinate: "))
y1 = int(input("Give the y1 coordinate: "))
x2 = int(input("Give the x2 coordinate: "))
y2 = int(input("Give the y2 coordinate: "))

length = 0
if x1 < x2:
    length = x2 - x1
else:
    length = x1 - x2

width = 0
if y1 < y2:
    width = y2 - y1
else:
    width = y1 - y2

area = 0
area = length * width

print(f'The area of your rectangle is {area}')