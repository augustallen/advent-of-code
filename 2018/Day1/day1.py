f = open(r"C:\Users\August\Documents\Advent of Code\Advent-of-Code-2018\Day1\day1_input.txt").readlines()

# example, uncomment to override file
# f = [-6, +3, +8, +5, -6] 

def part1():
    frequency = 0
    for i in f:
        frequency += int(i)
    return frequency

def part2():
    frequency = 0
    past_frequencies = {frequency} # set much faster than a list
    while True:   
        for i in f:
            frequency += int(i)
            if frequency in past_frequencies:
                return frequency
            past_frequencies.add(frequency)

print(part1())
print(part2())

# testing