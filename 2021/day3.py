with open("2021/day3.txt") as f:
    lines = [l.strip() for l in f]


def part1():
    gamma = ""
    epsilon = ""
    for digit in range(len(lines[0])):
        a = [int(i[digit]) for i in lines]
        mode = round(sum(a) / len(a))
        gamma += str(mode)
        epsilon += str(abs(mode-1))
    return int(gamma, 2) * int(epsilon, 2)


def part2():
    # Find oxygen
    oxygen_list = [l for l in lines]
    for digit in range(len(lines[0])):
        nth_digits = [int(i[digit]) for i in oxygen_list]
        average = sum(nth_digits) / len(nth_digits)
        if average == 0.5:
            keep = 1
        else:
            keep = round(average)
        oxygen_list = [i for i in oxygen_list if int(i[digit]) == keep]

    # Find co2
    co2_list = [l for l in lines]
    for digit in range(len(lines[0])):
        if len(co2_list) > 1:
            nth_digits = [int(i[digit]) for i in co2_list]
            average = sum(nth_digits) / len(nth_digits)
            if average == 0.5:
                keep = 1
            else:
                keep = round(average)
            co2_list = [i for i in co2_list if int(i[digit]) != keep]
    return int(oxygen_list[0], 2) * int(co2_list[0], 2)


print(f"Part 1: {part1()} \nPart 2: {part2()}")
