with open('2020/input_day4.txt') as f:
    lines = [l.strip() for l in f]

passports=[]
passport = ""
for line in lines:
    if not line: 
        passport = dict(p.split(":") for p in passport.lstrip().split(" "))
        passports.append(passport) 
        passport = ""
    passport += " "
    passport += line
passport = dict(p.split(":") for p in passport.lstrip().split(" "))
passports.append(passport)


valid_passports = 0
for p in passports:
    print(p)
    if p.keys() >= {"byr", "iyr", "eyr" ,"hgt", "hcl", "ecl", "pid"}:
        valid_passports += 1
    # else:
        #  print(f"Invalid passport:\n {p} \n {p.keys()}")
print(valid_passports)