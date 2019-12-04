l1 = [[1, 0], [2, 0], [3, 0]]
l2 = [[1, 2], [1, 0], [3, 0]]


new_l1 = set(tuple(row) for row in l1)
new_l2 = set(tuple(row) for row in l2)



print(new_l1)

cross_positions = set(new_l1).intersection(new_l2)


print(cross_positions)

cross_positions=[list(item) for item in cross_positions] 

print(cross_positions)

"""
l1 = [(1, 0), (2, 0), (3, 0)]
l2 = [(1, 2), (1, 0), (3, 0)]

cross_positions = set(l1).intersection(l2)

print(cross_positions)"""