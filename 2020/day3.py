with open('2020/input_day3.txt') as f:
    lines = [l.strip() for l in f]


def part1(lines):
    col = 0
    tree_count = 0
    for row in range(1,len(lines)): # starts on second row
        col += 3
        if col > 30:
            col -= 31
        if lines[row][col] == "#":
            tree_count+=1
    return tree_count

def tree_counter(lines, right, down):
    col = 0
    tree_count = 0
    for row in range(down,len(lines),down):
        col += right
        if col > 30:
            col -= 31
        if lines[row][col] == "#":
            tree_count+=1
    return tree_count

def part2(lines):
    return (tree_counter(lines,1,1) * 
            tree_counter(lines,3,1) *
            tree_counter(lines,5,1) *
            tree_counter(lines,7,1) *
            tree_counter(lines,1,2))

print(f"Part 1: {part1(lines)}\nPart 2: {part2(lines)}")