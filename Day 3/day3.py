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

print("starting cross_position identification")

# Method is incredibly slow (takes ~20 minutes to run, intersection of sets would be much faster but wouldn't store positions for part 2)
cross_positions=[]
for p1 in wire1_positions:
    for p2 in wire2_positions:       
        if p1 == p2:
            cross_positions.append(p1)

min_man=1000000000000 #dummy value defintion

for i in cross_positions:
    x = i[0]
    y = i[1]
    manhattan = abs(x) + abs(y)
    if manhattan<min_man:
        shortest_cross = [x,y]
        min_man = manhattan
print("Answer to part 1: " + str(min_man) + " which is found at point " + str(shortest_cross))

first_cross = cross_positions[0]

min_steps_wire1 = wire1_positions.index(first_cross)
min_steps_wire2 = wire2_positions.index(first_cross)
min_steps = min_steps_wire1 + min_steps_wire2 + 2 # Adding two to account for 0-index


print("Answer to part 2: " + str(min_steps) + " which is found at point " + str(first_cross))

print(cross_positions)
print(len(cross_positions))