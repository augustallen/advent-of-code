import re

with open('2020/input_day2.txt') as f:
    lines = [l.strip() for l in f]

def part1(lines):
    valid_passwords = 0
    for l in lines:
        m = re.search("(?P<min_count>\d+)-(?P<max_count>\d+)\s(?P<letter>\S):\s(?P<password>\S+)",l)
        count = m.group('password').count(m.group('letter'))
        if int(m.group('min_count')) <= count <= int(m.group('max_count')):
            valid_passwords += 1
    return valid_passwords

def part2(lines): 
    valid_passwords = 0
    for l in lines:
        m = re.search(r"(\d+)-(\d+)\s(\S):\s(\S+)",l)
        first_pos = int(m.group(1))
        second_pos = int(m.group(2))
        letter = m.group(3)
        password = m.group(4)
        if (password[first_pos-1] == letter and password[second_pos-1] != letter) or \
            (password[first_pos-1] != letter and password[second_pos-1] == letter):
            valid_passwords += 1
    return valid_passwords

print(f"Part 1 {part1(lines)}\nPart 2 {part2(lines)}")