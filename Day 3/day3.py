import re

with open(r"Day 3/input.txt","r") as f:
    values = f.read().split("\n")

wire1 = values[0].split(",")
wire2 = values[1].split(",")

def wire_movements(positions):
    x_position=0
    y_position=0
    wire_positions = []
    for value in positions:
        if value[0] == "R":
            for i in range(int(value[1:])):
                x_position += 1
                wire_x_y = [x_position,y_position]
                wire_positions.append(wire_x_y[:])
        if value[0] == "L":
            for i in range(int(value[1:])):
                x_position -= 1
                wire_x_y = [x_position,y_position]
                wire_positions.append(wire_x_y[:])
        if value[0] == "U":
            for i in range(int(value[1:])):
                y_position += 1
                wire_x_y = [x_position,y_position]
                wire_positions.append(wire_x_y[:])
        if value[0] == "D":
            for i in range(int(value[1:])):
                y_position -= 1
                wire_x_y = [x_position,y_position]
                wire_positions.append(wire_x_y[:])
    return wire_positions


wire1_positions = wire_movements(wire1)
wire2_positions = wire_movements(wire2)

cross_positions=[]

for p1 in wire1_positions:
    for p2 in wire2_positions:       
        if p1 == p2:
            cross_positions.append(p1)
print(cross_positions)

print(type(cross_positions))
for i in cross_positions:
    x=abs(i[0])
    y=abs(i[1])
    print(x+y)



    