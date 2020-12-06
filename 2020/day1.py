with open('2020/input_day1.txt') as f:
    lines = [int(l.strip()) for l in f]

def attempt1_p1(lines):
    for l1 in lines:
        for l2 in lines:
            if l1+l2 == 2020:
               return l1*l2
    return "No two values sum to 2020."

def attempt1_p2(lines):
    for l1 in lines:
        for l2 in lines:
            for l3 in lines:
                if l1+l2+l3 == 2020:
                    return l1*l2*l3
    return "No three values sum to 2020."

print(f"Part 1 {attempt1_p1(lines)}\nPart 2 {attempt1_p2(lines)}")