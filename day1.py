# solutions dsasadfdsa
import math

f = open("day1_module_mass.txt","r")


total_fuel_required = 0
fuel_per_module = 0

for mass in f:
    fuel_per_module = math.floor(int(mass)/3) - 2
    additional_fuel = math.floor(int(fuel_per_module)/3) - 2    
    while additional_fuel>0:
      fuel_per_module += additional_fuel
      additional_fuel = math.floor(int(additional_fuel)/3) - 2
    total_fuel_required += fuel_per_module

print(total_fuel_required)