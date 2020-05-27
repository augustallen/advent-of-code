# Day 3 - December 4, 2019
# Andrea Mazzocchi

# Star 1 - Create Grid and Find Where Two Wires Cross

import pandas as pd
import numpy as np
from scipy import stats
import math

wire_1 = pd.read_csv('Day 3/Andrea Day 3/wire_1.csv') # replace wire_1.csv with practice_1-1.csv, practice_2-1.csv, or practice_3-1.csv
wire_1['Steps'] = wire_1['Steps'].str[1:].astype(int)
wire_1['Direction'] = wire_1['Direction'].str.replace(r'\d+', '')
wire_2 = pd.read_csv('Day 3/Andrea Day 3/wire_2.csv') # replace wire_2.csv with practice_1-2.csv, practice_2-2.csv, or practice_3-2.csv
wire_2['Steps'] = wire_2['Steps'].str[1:].astype(int)
wire_2['Direction'] = wire_2['Direction'].str.replace(r'\d+', '')



i = 0
for i in range(len(wire_1['Direction'])): # This length is the number of movements the wire takes (9 in the case of wire 1 in practice 1)
    if wire_1.at[i,'Direction'] == 'U':
        if i > 0:
            wire_1.at[i,'Position Y'] = wire_1.at[i,'Steps'] + wire_1.at[(i-1),'Position Y']
            wire_1.at[i,'Position X'] = wire_1.at[i-1,'Position X']
        else:
            wire_1.at[i,'Position Y'] = wire_1.at[i,'Steps']
    if wire_1.at[i,'Direction'] == 'D':
        if i > 0:
            wire_1.at[i,'Position Y'] = wire_1.at[i-1,'Position Y'] - wire_1.at[i,'Steps']
            wire_1.at[i,'Position X'] = wire_1.at[i-1,'Position X']
        else:
            wire_1.at[i,'Position Y'] = -wire_1.at[i,'Steps']
    if wire_1.at[i,'Direction'] == 'R':
        if i > 0:
            wire_1.at[i,'Position X'] = wire_1.at[i,'Steps'] + wire_1.at[(i-1),'Position X']
            wire_1.at[i,'Position Y'] = wire_1.at[i-1,'Position Y']
        else:
            wire_1.at[i,'Position X'] = wire_1.at[i,'Steps']
    if wire_1.at[i,'Direction'] == 'L':
        if i > 0:
            wire_1.at[i,'Position X'] = wire_1.at[i-1,'Position X'] - wire_1.at[i,'Steps']
            wire_1.at[i,'Position Y'] = wire_1.at[i-1,'Position Y']
        else:
            wire_1.at[i,'Position X'] = -wire_1.at[i,'Steps']
    i +=1

i = 0
for i in range(len(wire_2['Direction'])): # This length is the number of movements the wire takes (9 in the case of wire 1 in practice 1)
    if wire_2.at[i,'Direction'] == 'U':
        if i > 0:
            wire_2.at[i,'Position Y'] = wire_2.at[i,'Steps'] + wire_2.at[(i-1),'Position Y']
            wire_2.at[i,'Position X'] = wire_2.at[i-1,'Position X']
        else:
            wire_2.at[i,'Position Y'] = wire_2.at[i,'Steps']
    if wire_2.at[i,'Direction'] == 'D':
        if i > 0:
            wire_2.at[i,'Position Y'] = wire_2.at[i-1,'Position Y'] - wire_2.at[i,'Steps']
            wire_2.at[i,'Position X'] = wire_2.at[i-1,'Position X']
        else:
            wire_2.at[i,'Position Y'] = -wire_2.at[i,'Steps']
    if wire_2.at[i,'Direction'] == 'R':
        if i > 0:
            wire_2.at[i,'Position X'] = wire_2.at[i,'Steps'] + wire_2.at[(i-1),'Position X']
            wire_2.at[i,'Position Y'] = wire_2.at[i-1,'Position Y']
        else:
            wire_2.at[i,'Position X'] = wire_2.at[i,'Steps']
    if wire_2.at[i,'Direction'] == 'L':
        if i > 0:
            wire_2.at[i,'Position X'] = wire_2.at[i-1,'Position X'] - wire_2.at[i,'Steps']
            wire_2.at[i,'Position Y'] = wire_2.at[i-1,'Position Y']
        else:
            wire_2.at[i,'Position X'] = -wire_2.at[i,'Steps']
    i +=1
        
# print(wire_2) 

# new stuff

r = 0
i = 0
j = 0 
manhattan_distances = [] # Added by August
i_values = []

for j in range(len(wire_2['Position X'])-1):
    for i in range(len(wire_1['Position X'])-1):
        a = wire_2.at[j, 'Position X']
        b = wire_1.at[i, 'Position X']
        c = wire_1.at[i+1, 'Position X']
        if  b <= a <= c or c <= a <= b:
            e = wire_1.at[i, 'Position Y']
            f = wire_2.at[j, 'Position Y']
            g = wire_2.at[j+1,'Position Y']
            if  f <= e <= g or g <= e <= f:
                d = abs(e) + abs(a)
                manhattan_distances.append(d)     
                i_values.append(i)
        i += 1
    j += 1


i = 0
j = 0 

for j in range(len(wire_2['Position Y'])-1):
    for i in range(len(wire_1['Position Y'])-1):
        a = wire_2.at[j, 'Position Y']
        b = wire_1.at[i, 'Position Y']
        c = wire_1.at[i+1, 'Position Y']
        if  b <= a <= c or c <= a <= b:
            e = wire_1.at[i, 'Position X']
            f = wire_2.at[j, 'Position X']
            g = wire_2.at[j+1,'Position X']
            if  f <= e <= g or g <= e <= f:
                d = abs(e) + abs(a)
                manhattan_distances.append(d)
                i_values.append(i)
        i += 1
    j += 1

manhattan_distances.sort()
i_values.sort()

print(manhattan_distances)
print(i_values)
