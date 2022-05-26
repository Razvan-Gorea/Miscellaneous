#!/usr/bin/env python3

#2,4,8,16,32
#1,2,3,4,5

num_of_gen = int(input("Number of generations:" ))
num_of_ancestors = 2 * (2 ** (num_of_gen - 1))
print(num_of_ancestors)