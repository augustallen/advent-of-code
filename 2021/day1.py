with open("2021/day1.txt") as f:
    lines = [int(l.strip()) for l in f]


def part1():
    increases = 0
    for i, l in enumerate(lines):
        if l > lines[i-1] and i > 0:
            increases += 1
    return increases


def part2():
    increases = 0
    for i, l in enumerate(lines):
        if lines[i] > lines[i-3] and i > 2:
            increases += 1
    return increases


print(f"Part 1: {part1()} \nPart 2: {part2()}")
