import numpy as np

lines_with_newline = open(r"C:\Users\August\Documents\Advent of Code\Advent-of-Code-2018\Day2\day2_input.txt").readlines()
lines = []
for line in lines_with_newline:
    line_stripped = line.rstrip("\n")
    lines.append(line_stripped)

def part1():
    n_exactly_two = 0
    n_exactly_three = 0
    for line in lines:
        (unique,counts) = np.unique(list(line),return_counts=True)
        if 2 in counts:
            n_exactly_two += 1
        if 3 in counts:
            n_exactly_three += 1
    return n_exactly_three * n_exactly_two



def part2():
    differences = []
    for current_line in lines:
       for line_compare in lines:
            diff_count = 0
            u = zip(current_line,line_compare)
            for t1,t2 in u:
                if t1 != t2:
                    diff_count += 1
            if diff_count == 1:
                rezip = zip(current_line,line_compare)
                identical_chars = ''
                for t1, t2 in rezip:
                    if t1 == t2:
                        identical_chars += t1
                output = f'Difference count of 1 between current line {current_line} and line_compare {line_compare} with identical_characters {identical_chars}.'
                return identical_chars

print(part1())
print(part2())

# testing