from collections import defaultdict


def same_adjacent2(number): # If there are 2 of anything, they would have to be next to each other in order to also pass the never_decrease function
    d = defaultdict(int)
    for digit in str(number):
        d[digit] += 1

    return (2 in d.values())

print(same_adjacent2(111122))


def same_adjacent_fails(number):
    counter=0
    for char in str(number):
        if counter<(len(str(number))-1): # Skip if counter is on last character
            counter += 1
            char_after = str(number)[counter]
            if char == char_after:
                if counter == (len(str(number))-1):
                    return True
                if char == str(number)[counter+1] and counter == len(str(number)):
                    return False
                return True
    return False


def same_adjacent_fails2(number):
    counter=0
    for char in str(number):
        if counter<(len(str(number))-1):
            counter += 1
        
            if char == str(number)[counter]:
                if counter == (len(str(number))-1):
                    return True
                if char == str(number)[counter+1]:
                    return False
    return False



