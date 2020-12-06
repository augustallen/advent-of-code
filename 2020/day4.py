import re

with open('2020/input_day4.txt') as f:
    lines = [l.strip() for l in f]


def format_passport(lines):
    passports=[]
    passport = ""
    for line in lines:
        if not line: # on an empty line reset the current passport after saving all it's k:v pairs
            passport = dict(p.split(":") for p in passport.lstrip().split(" "))
            passports.append(passport) 
            passport = ""
        passport += " "
        passport += line
    # next two lines are for last passport only
    passport = dict(p.split(":") for p in passport.lstrip().split(" "))
    passports.append(passport)
    return passports

def part1(lines):
    passports = format_passport(lines)
    valid_passports = 0
    for p in passports:
        if p.keys() >= {"byr", "iyr", "eyr" ,"hgt", "hcl", "ecl", "pid"}:
            valid_passports += 1
    return valid_passports

def part2(lines):
    passports = format_passport(lines)
    valid_passports = 0
    for p in passports:
        if p.keys() >= {"byr", "iyr", "eyr" ,"hgt", "hcl", "ecl", "pid"}:
            if (1920 <= int(p['byr']) <= 2002 and
                2010 <= int(p['iyr']) <= 2020 and 
                2020 <= int(p['eyr']) <= 2030 and 
                re.match(r"#[a-f0-9]{6}",p['hcl']) and 
                p['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth'] and
                re.match(r"^\d{9}$",p['pid'])): # need ^ for start of string and $ for end of string to force only 9-digits
                    m = re.search(r"(\d+)(\w+)",p['hgt'])
                    if ((m.group(2) == 'cm' and 150 <= int(m.group(1)) <= 193) 
                        or (m.group(2) == 'in' and 59 <= int(m.group(1)) <= 76)):
                        valid_passports += 1
    return valid_passports

print(f"Part 1: {part1(lines)}\nPart 2: {part2(lines)}")