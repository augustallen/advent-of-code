import re

with open('2020/input_day7.txt') as f:
    lines = [l.strip() for l in f]
    
# Format lines into dictionary with outer bag strings as the key
# and inner bag list of strings as the value
bags = {}
for line in lines:
    split = line.split(" contain ")
    outer = re.search(r"(^\w+ \w+)",split[0]).group(1)
    inner = []
    if not re.search(r"^no",split[1]): # keeps empty list for inner bags if false
        for b in split[1].split(", "):
            m = re.search(r"\d+ (\w+ \w+) ",b)
            inner.append(m.group(1))
    bags.update({outer : inner})
    

# From https://www.python.org/doc/essays/graphs/   
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

# Take all possible bag (keys) and identify if there is a path to contain the shiny gold bag
possible_outer_bags = 0
for key in bags:
    paths = find_all_paths(bags, key, 'shiny gold')
    if not key =='shiny gold' and len(paths)>0:
        possible_outer_bags += 1
        print(f"Possible outer bag {key} with path(s): {paths}")

print(possible_outer_bags)


