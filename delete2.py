def same_adjacent2(number):
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

print(same_adjacent2(111122))

#print(len(str(1234)))
