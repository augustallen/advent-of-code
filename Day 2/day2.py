import traceback

with open(r"Day 2/input.txt","r") as f:
    values = f.read().split(",")

# Convert values in the list to integers.
values = map(int, values)
values = list(map(int, values))

"""
# Working function for answer 1 but not answer 2, going to adjust from while loop to for loop to try and avoid index out of range issues
def opcode_func(input_list,noun,verb):
    values[1] = noun
    values[2] = verb
    pointer = 0
    opcode=input_list[pointer]
    while opcode!=99:
        if opcode == 1:
            input_list[input_list[pointer+3]] = input_list[input_list[pointer+1]] + input_list[input_list[pointer+2]]
        if opcode == 2:
            input_list[input_list[pointer+3]] = input_list[input_list[pointer+1]] * input_list[input_list[pointer+2]]
        pointer += 4
        opcode=input_list[pointer]
    return input_list, pointer
"""

def opcode_func(input_list,noun,verb):
    values[1] = noun
    values[2] = verb
    
    for pointer in range(0,len(input_list),4):
        opcode = input_list[pointer]
        if opcode == 1:
            input_list[input_list[pointer+3]] = input_list[input_list[pointer+1]] + input_list[input_list[pointer+2]]
        if opcode == 2:
            input_list[input_list[pointer+3]] = input_list[input_list[pointer+1]] * input_list[input_list[pointer+2]]
        if opcode == 99:
            break
        opcode=input_list[pointer]
    return input_list, pointer



print("Answer to part 1: " + str(opcode_func(values,12,2)[0][0]))

"""
for noun in range(0,99):
    try:
        output,pointer = (opcode_func(values,noun,2))
    except:
        print("Input broke on noun " + str(noun) + ", pointer " + str(pointer) + ", and output: " + str(output))
        print("")
        traceback.print_exc()
        break
        #if opcode_func(values,noun,verb)[0] == 19690720:
    #    break
    #else:
    #    continue
    #break
"""




"""
edited_values = values

print(values)
print(edited_values)
while edited_values[0] != 19690720:
    while opcode!=99:
                if opcode == 1:
                    edited_values[edited_values[pointer+3]] = edited_values[edited_values[pointer+1]] + edited_values[edited_values[pointer+2]]
                if opcode == 2:
                    edited_values[edited_values[pointer+3]] = edited_values[edited_values[pointer+1]] * edited_values[edited_values[pointer+2]]
                pointer += 4
                opcode=edited_values[pointer]
    edited_values = values                          # Re-set edited values
    for noun in range(0,99):                        # Cycle through all possible options for value 1, but need to figure out how to break if edited_values[0] = 19690720
        values[1] = noun
        for verb in range(0,99):
            values[2] = verb
"""