# set up
import re
keys = []
locks = []
with open('Day25.input', 'r') as file:
    lines = file.readlines()

lineNum = 0
while lineNum < len(lines):
    values = [0,0,0,0,0]
    for index in range(lineNum, lineNum + 7):
        for index2 in range(0,5):
            if lines[index][index2] == '#':
                values[index2] += 1
    if lines[lineNum][0] == '#':
        keys.append(values)
    else:
        locks.append(values)
    lineNum += 8

# silver 
fit = 0
for key in keys:
    for lock in locks:
        if key[0] + lock[0] <= 7 and \
            key[1] + lock[1] <= 7 and \
            key[2] + lock[2] <= 7 and \
            key[3] + lock[3] <= 7 and \
            key[4] + lock[4] <= 7:
                fit += 1
print(fit)