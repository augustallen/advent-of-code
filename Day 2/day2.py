with open(r"Day 2\input.txt","r") as f:
    values = f.read().split(",")

#Convert values in the list to integers.
values = map(int, values)
values = list(map(int, values))

# Start at first opcode 
iterator = 0
opcode=values[iterator]

while opcode!=99:
    if opcode == 1:
        values[values[iterator+3]] = values[values[iterator+1]] + values[values[iterator+2]]
    if opcode == 2:
        values[values[iterator+3]] = values[values[iterator+1]] * values[values[iterator+2]]
    iterator += 4
    opcode=values[iterator]

print(values)