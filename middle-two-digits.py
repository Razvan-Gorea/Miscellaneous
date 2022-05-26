#!/usr/bin/env python3

num = int(input())

first_middle = ((num // 1000) % 10) * 10
second_middle = (num // 100) % 10
middle = first_middle + second_middle

print(middle)
