input = 'R4, R3, L3, L2, L1, R1, L1, R2, R3, L5, L5, R4, L4, R2, R4, L3, R3, L3, R3, R4, R2, L1, R2, L3, L2, L1, R3, R5, L1, L4, R2, L4, R3, R1, R2, L5, R2, L189, R5, L5, R52, R3, L1, R4, R5, R1, R4, L1, L3, R2, L2, L3, R4, R3, L2, L5, R4, R5, L2, R2, L1, L3, R3, L4, R4, R5, L1, L1, R3, L5, L2, R76, R2, R2, L1, L3, R189, L3, L4, L1, L3, R5, R4, L1, R1, L1, L1, R2, L4, R2, L5, L5, L5, R2, L4, L5, R4, R4, R5, L5, R3, L1, L3, L1, L1, L3, L4, R5, L3, R5, R3, R3, L5, L5, R3, R4, L3, R3, R1, R3, R2, R2, L1, R1, L3, L3, L3, L1, R2, L1, R4, R4, L1, L1, R3, R3, R4, R1, L5, L2, R2, R3, R2, L3, R4, L5, R1, R4, R5, R4, L4, R1, L3, R1, R3, L2, L3, R1, L2, R3, L3, L1, L3, R4, L4, L5, R3, R5, R4, R1, L2, R3, R5, L5, L4, L1, L1'.split(",")
input = [x.strip(' ') for x in input] #strip spaces

def part1():
    x,y=0,0
    current_direction = "N"

    for i in input:
        if i[0] == "R" and current_direction=="N":
            current_direction = "E"
            x += int(i[1:])
            continue
        if i[0] == "R" and current_direction=="E":
            current_direction = "S"
            y -= int(i[1:])
            continue
        if i[0]=="R" and current_direction=="S":   
            current_direction = "W"
            x -= int(i[1:])
            continue
        if i[0]=="R" and current_direction=="W":
            current_direction = "N"
            y += int(i[1:])
            continue
        if i[0] == "L" and current_direction=="N":
            current_direction = "E"
            x += int(i[1:])
            continue
        if i[0] == "L" and current_direction=="W":
            current_direction = "S"
            y -= int(i[1:])
            continue
        if i[0]=="L" and current_direction=="S":   
            current_direction = "W"
            x -= int(i[1:])
            continue
        if i[0]=="L" and current_direction=="E":
            current_direction = "N"
            y += int(i[1:])
            continue

    return f"The final destination is located at {x,y} which is {abs(x)+abs(y)} blocks away."

print(part1())