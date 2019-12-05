# It is a six-digit number. Implicit in my range which all have six digits but useful for other ranges.

def length_six(number):
    if (len(str(number))) == 6:
        return True
    return False

# Two adjacent digits are the same (like 22 in 122345).

def same_adjacent(number):
    counter=0
    for char in str(number):
        if counter<(len(str(number))-1):
            counter += 1
            if char == str(number)[counter]:
                return True
    return False

# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

def never_decrease(number):
    counter = 0
    for char in str(number):
        if counter<(len(str(number))-1):
            counter += 1
            if char > str(number)[counter]:
                return False
    return True

# Solving part 1.

possible_count1 = 0

for password in range(138241,674035):
    if length_six(password) and same_adjacent(password) and never_decrease(password):
        possible_count1 += 1

print("The answer to part 1: " + str(possible_count1))

# Solving part 2.

def same_adjacent2(number):
    counter=0
    for char in str(number):
        if counter<(len(str(number))-1):
            counter += 1
            char_after = str(number)[counter]
            char_before = str(number)[counter-2]
            if char == char_after:
                if counter>1 and not char == char_before:
                    continue
                if not char == char_before:
                    return True
    return False

possible_count2 = 0

for password in range(138241,674035):
    if length_six(password) and same_adjacent2(password) and never_decrease(password):
        possible_count2 += 1


print("The answer to part 2: " + str(possible_count2))