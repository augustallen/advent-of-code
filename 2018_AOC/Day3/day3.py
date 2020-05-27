lines_with_newline = open("Day3/input.txt").readlines()
lines = []
for line in lines_with_newline:
    line_stripped = line.rstrip("\n")
    lines.append(line_stripped)

print(lines)