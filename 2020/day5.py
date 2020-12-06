import math

with open('2020/input_day5.txt') as f:
    lines = [l.strip() for l in f]

def part1(lines):
    seat_ids = []
    for l in lines:
        row_min = 0
        row_max = 127
        col_min = 0
        col_max = 7
        for char in l:    
            mid_row = math.ceil((row_max-row_min)/2)
            mid_col = math.ceil((col_max-col_min)/2)
            if char == 'B':
                row_min = row_min + mid_row
            if char == 'F':
                row_max = row_max - mid_row
            if char == 'R':  
                col_min = col_min + mid_col
            if char == 'L':  
                col_max = col_max - mid_col
            seat_id = row_min * 8 + col_min
        seat_ids.append(seat_id)
    return max(seat_ids)        

def part2(lines):
    seats = {}
    for l in lines:
        row_min = 0
        row_max = 127
        col_min = 0
        col_max = 7
        for char in l:    
            mid_row = math.ceil((row_max-row_min)/2)
            mid_col = math.ceil((col_max-col_min)/2)
            if char == 'B':
                row_min = row_min + mid_row
            if char == 'F':
                row_max = row_max - mid_row
            if char == 'R':  
                col_min = col_min + mid_col
            if char == 'L':  
                col_max = col_max - mid_col
            seat_id = row_min * 8 + col_min
        seats[seat_id] = [row_min, col_min]

    seat_ids = set(list(seats.keys()))
    my_seat_id = set(range(min(seat_ids),max(seat_ids))) - seat_ids
    return next(iter(my_seat_id))

print(f"Part 1: {part1(lines)}\nPart 2: {part2(lines)}")