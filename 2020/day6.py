from collections import Counter

with open('2020/input_day6.txt') as f:
    lines = [l.strip() for l in f]
    lines.append('')

def part1(lines):
    group = []
    yes_counter = 0

    for l in lines:
        if not l:
            yes_counter += len(set(group))
            group = []
        for q in l:
            group.append(q)
    return yes_counter


def part2(lines):
    group = []
    ppl_in_group = 0
    yes_counter = 0

    for l in lines:
        if l:
            ppl_in_group += 1
            for q in l:
                group.append(q)
        else:
            count_per_letter = {i:group.count(i) for i in group}
            values = list(count_per_letter.values())
            # Count matches for each letter with the number of ppl
            answer = values.count(ppl_in_group)
            yes_counter += answer
            group = [] 
            ppl_in_group = 0
    return yes_counter

print(f"Part 1: {part1(lines)}\nPart 2: {part2(lines)}")