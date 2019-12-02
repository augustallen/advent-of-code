import math

# File provided at: https://adventofcode.com/2019/day/1
file_path="Day 1\day1_module_mass.txt"

f = open(file_path,"r")
total_fuel_required = 0

for mass in f:
    total_fuel_required += math.floor(int(mass)/3) - 2

print("Answer to Part 1: " + str(total_fuel_required))

f.close()

# Re-open file to re-iterate through the ffor loop, this time accounting for mass of fuel.
f = open(file_path,"r")

total_fuel_required = 0
fuel_per_module = 0

for mass in f:
    fuel_per_module = math.floor(int(mass)/3) - 2
    additional_fuel = math.floor(int(fuel_per_module)/3) - 2    
    while additional_fuel>0:
      fuel_per_module += additional_fuel
      additional_fuel = math.floor(int(additional_fuel)/3) - 2
    total_fuel_required += fuel_per_module

print("Answer to Part 2: " + str(total_fuel_required))

f.close()