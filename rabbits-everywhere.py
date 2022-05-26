#!/usr/bin/env python3

start_pop = int(input("Give the initial rabbit population: "))
num_of_years = int(input("Number of years of reproduction: "))
final_pop = start_pop * (2 ** num_of_years)
print(f'Final rabbit population: {final_pop}')