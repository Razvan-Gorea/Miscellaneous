#!/usr/bin/env python3

num = int(input())

part1 = ((num // 100000) % 10) * 1000
part2 = ((num // 10000) % 10) * 100
part3 = ((num // 1000) % 10) * 100000
part4 = ((num // 100) % 10) * 10000
part5 = num % 100

new_date = part1 + part2 + part3 + part4 + part5

print(new_date)
