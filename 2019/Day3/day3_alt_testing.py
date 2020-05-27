# Alternative, and much faster, solution from: # https://www.reddit.com/r/adventofcode/comments/e5bz2w/2019_day_3_solutions/f9lx87q/

with open("Day 3/input.txt", "r") as f:
    data = f.read().rstrip()

data = [[(x[0], int(x[1:])) for x in line.split(",")] for line in data.splitlines()]


def points(dirs):
    points = []
    x, y = 0, 0
    for d, c in dirs:
        if d == "U":
            points.extend((x, y + i) for i in range(1, c + 1))
            y += c
        if d == "D":
            points.extend((x, y - i) for i in range(1, c + 1))
            y -= c
        if d == "L":
            points.extend((x - i, y) for i in range(1, c + 1))
            x -= c
        if d == "R":
            points.extend((x + i, y) for i in range(1, c + 1))
            x += c
    return points

def part1(data):
    a, b = data
    pa = points(a)
    pb = points(b)

    union = set(pa).intersection(pb)

    result = min(union, key=(lambda pos: abs(pos[0]) + abs(pos[1])))

    return sum(abs(x) for x in result), pa

print(part1(data))