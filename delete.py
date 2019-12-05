def same_adjacent2(number):
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

print(same_adjacent2(12256))

#print(len(str(1234)))
