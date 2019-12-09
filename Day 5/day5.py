import traceback

with open(r"Day 5/input_test.txt","r") as f:
    values = f.read().split(",")

# Convert values in the list to integers.
values = map(int, values)
values = list(map(int, values))

def opcode_func(input_list):
    pointer=0
    while pointer<len(values):
        opcode = input_list[pointer]
        print(input_list)
        if opcode == 1:
            input_list[input_list[pointer+3]] = input_list[input_list[pointer+1]] + input_list[input_list[pointer+2]]           
        if opcode == 2:
            input_list[input_list[pointer+3]] = input_list[input_list[pointer+1]] * input_list[input_list[pointer+2]]
        if opcode == 3:
            print(input_list[input_list[pointer+1]])
            print(input_list[pointer+1])
            input_list[input_list[pointer+1]] = input_list[pointer+1]
        if opcode == 99:
            break
        pointer += 1 # needs to be incremented by the number of instructions
    return input_list

# Assign the list of values to be an editable list (without the colon slicing the list both variables would reference the same list)
editable_values=values[:] 


print(opcode_func(editable_values))