with open('2020/input_day4.txt') as f:
    lines = [l.strip() for l in f]


def part1(lines):
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

    valid_passports = 0
    for p in passports:
        if p.keys() >= {"byr", "iyr", "eyr" ,"hgt", "hcl", "ecl", "pid"}:
            valid_passports += 1
    return valid_passports

print(part1(lines))