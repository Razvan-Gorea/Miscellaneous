#!/usr/bin/env python3

num = int(input("Give a number: "))
first = 0
first = (num // 100) % 10

second = 0
second = (num // 10) % 10

third = 0
third = num % 10

print(first)
print(second)
print(third)