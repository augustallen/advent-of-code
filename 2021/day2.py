with open("2021/day2.txt") as f:
    lines = [(s.split()[0], int(s.split()[1])) for s in f]


def part1():
    horizontal = 0
    depth = 0
    for l in lines:
        if l[0] == 'forward':
            horizontal += l[1]
        if l[0] == 'up':
            depth -= l[1]
        if l[0] == 'down':
            depth += l[1]
    return horizontal*depth


def part2():
    aim = 0
    horizontal = 0
    depth = 0
    for l in lines:
        if l[0] == 'forward':
            horizontal += l[1]
            depth += aim * l[1]
        if l[0] == 'up':
            aim -= l[1]
        if l[0] == 'down':
            aim += l[1]
        print(horizontal, depth, aim)
    return horizontal*depth


print(f"Part 1: {part1()} \nPart 2: {part2()}")
