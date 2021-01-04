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
    if not re.search(r"^no",split[1]): # keeps empty list when there are no inner bags
        for b in split[1].split(", "):
            m = re.search(r"(\d+) (\w+ \w+) ",b)
            inner.append({m.group(2) : m.group(1)})
    bags.update({outer : inner})
    

# https://www.python.org/doc/essays/graphs/   
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        for bag in node: # node is a dictionary of bag : quantity and we just want the bag
            if bag not in path:
                newpaths = find_all_paths(graph, bag, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
    return paths

# Take all possible bag (keys) and identify if there is a path to contain the shiny gold bag

def part1():
    possible_outer_bags = 0
    for key in bags:
        paths = find_all_paths(bags, key, 'shiny gold')
        if not key =='shiny gold' and len(paths)>0:
            possible_outer_bags += 1
    return possible_outer_bags






def bags_for_days(outer_bag,outer_bag_count,running_total):
    for node in bags[outer_bag]:
        for inner_bag in node:
            inner_bag_count = int(node[inner_bag])
            additional_bags = outer_bag_count*inner_bag_count
            running_total += additional_bags
            print(f"The {outer_bag_count} {outer_bag} contains {inner_bag_count} {inner_bag} which is {additional_bags} additional bags for a running total of {running_total}.")
            bags_for_days(outer_bag=inner_bag,outer_bag_count=inner_bag_count,running_total=running_total)
    return running_total
print(bags_for_days('shiny gold',1,0))

# print(find_minimum_bags(bags, 'shiny gold'))
