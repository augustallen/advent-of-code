import re

with open(r"Day 3/input.txt","r") as f:
    values = f.read().split("\n")

wire1 = values[0].split(",")
wire2 = values[1].split(",")

def wire_movements(positions):
    wire_x_y = [0,0]
    wire_positions = []
    for value in positions:
        if value[0] == "R":
            wire_x_y[0] += int(value[1:])
        if value[0] == "L":
            wire_x_y[0] -= int(value[1:])
        if value[0] == "U":
            wire_x_y[1] += int(value[1:])
        if value[0] == "D":
            wire_x_y[1] -= int(value[1:])
        wire_positions.append(wire_x_y[:])
    return wire_positions


wire1_positions = wire_movements(wire1)
wire2_positions = wire_movements(wire2)
print(wire1_positions)
print(wire2_positions)


for p1 in wire1_positions:
    for p2 in wire2_positions:       
        if p1 == p2:
            print("Wires cross at: " + p1 + " " + p2) 
        
    