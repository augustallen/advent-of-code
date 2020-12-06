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

print(part1(lines))