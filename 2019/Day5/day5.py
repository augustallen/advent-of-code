import traceback

with open(r"Day 5/input.txt","r") as f:
    values = f.read().split(",")

# Convert values in the list to integers.
values = map(int, values)
values = list(map(int, values))

def opcode_func(input_list,noun,verb):
    input_list[1] = noun
    input_list[2] = verb
    for pointer in range(0,len(input_list),4):
        opcode = input_list[pointer]
        if opcode == 1:
            input_list[input_list[pointer+3]] = input_list[input_list[pointer+1]] + input_list[input_list[pointer+2]]
        if opcode == 2:
            input_list[input_list[pointer+3]] = input_list[input_list[pointer+1]] * input_list[input_list[pointer+2]]
        if opcode == 99:
            break
        opcode=input_list[pointer]
    return input_list

# Assign the list of values to be an editable list (without the colon slicing the list both variables would reference the same list)
editable_values=values[:] 

print("Answer to part 1: " + str(opcode_func(editable_values,12,2)[0]))

for noun in range(100):
    for verb in range(100):
        editable_values = values[:]                             
        output = (opcode_func(editable_values,noun,verb))
        if output[0] == 19690720:
            print("Answer to part 2: " + str(100*noun+verb))