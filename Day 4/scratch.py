from collections import defaultdict

words = "apple banana apple strawberry banana lemon"

number = 123455

d = defaultdict(int)
for digit in str(number):
    d[digit] += 1

print(d)

'''  
def same_adjacent2(number):
    counter=0
    for char in str(number):
        if counter<(len(str(number))-1):
            counter += 1
            char_after = str(number)[counter]
            char_before = str(number)[counter-2]
            if counter>1 and char == char_after and not char == char_before:
                return True
    return False
'''
# print(same_adjacent2(111222))


# maybe write it a different way to just count the quantity of each number and search for numbers where there's at least one 2?