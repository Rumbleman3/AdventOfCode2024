# Set up
import re
map = []
instructions = ''
with open('Day15.input', 'r') as file:
    fillingMap = True
    for line in file:
        if line == '\n':
            fillingMap = False
        if fillingMap:
            line = line.replace('\n', '')
            map.append(line)
        else:
            line = line.replace('\n', '')
            instructions += line

# Silver star
roboti = 0
robotj = 0
for i in range(0, len(map)):
    for j in range(0, len(map[i])):
        if map[i][j] == '@':
            roboti = i
            robotj = j

for i in range(0, len(instructions)):
    instruction = instructions[i]
    if instruction == '^':
        # find the first empty space
        starti = roboti - 1
        while (starti > 0) and map[starti][robotj] == 'O':
            starti -= 1
        # move the blocks if possible
        if (starti > 0) and map[starti][robotj] == '.':
            map[starti] = map[starti][:robotj] + 'O' + map[starti][robotj+1:]
            map[roboti - 1] = map[roboti - 1][:robotj] + '@' + map[roboti - 1][robotj+1:]
            map[roboti] = map[roboti][:robotj] + '.' + map[roboti][robotj+1:]
            roboti = roboti - 1
    elif instruction == 'v':
        # find the first empty space
        starti = roboti + 1
        while (starti <= len(map)) and map[starti][robotj] == 'O':
            starti += 1
        # move the blocks if possible
        if (starti <= len(map)) and map[starti][robotj] == '.':
            map[starti] = map[starti][:robotj] + 'O' + map[starti][robotj+1:]
            map[roboti + 1] = map[roboti + 1][:robotj] + '@' + map[roboti + 1][robotj+1:]
            map[roboti] = map[roboti][:robotj] + '.' + map[roboti][robotj+1:]
            roboti = roboti + 1
    elif instruction == '<':
        # find the first empty space
        startj = robotj - 1
        while (startj > 0) and map[roboti][startj] == 'O':
            startj -= 1
        # move the blocks if possible
        if (startj > 0) and map[roboti][startj] == '.':
            map[roboti] = map[roboti][:startj] + 'O' + map[roboti][startj + 1:]
            map[roboti] = map[roboti][:robotj - 1] + '@' + map[roboti][robotj:]
            map[roboti] = map[roboti][:robotj] + '.' + map[roboti][robotj+1:]
            robotj = robotj - 1
    elif instruction == '>':
        # find the first empty space
        startj = robotj + 1
        while (startj <= len(map)) and map[roboti][startj] == 'O':
            startj += 1
        # move the blocks if possible
        if (startj <= len(map)) and map[roboti][startj] == '.':
            map[roboti] = map[roboti][:startj] + 'O' + map[roboti][startj + 1:]
            map[roboti] = map[roboti][:robotj + 1] + '@' + map[roboti][robotj + 2:]
            map[roboti] = map[roboti][:robotj] + '.' + map[roboti][robotj+1:]
            robotj = robotj + 1

gps = 0
for i in range(0, len(map)):
    for j in range(0, len(map[i])):
        if map[i][j] == 'O':
            gps += 100 * i + j
print(gps)

# Gold star
map = []
instructions = ''
with open('Day15.input', 'r') as file:
    fillingMap = True
    for line in file:
        if line == '\n':
            fillingMap = False
        if fillingMap:
            line = line.replace('\n', '')
            map.append(line)
        else:
            line = line.replace('\n', '')
            instructions += line

map2 = []
for i in range(0, len(map)):
    map2.append([])
    for j in range(0, len(map[i])):
        if map[i][j] == '#' or map[i][j] == '.':
            map2[i].append(map[i][j])
            map2[i].append(map[i][j])
        elif map[i][j] == 'O':
            map2[i].append('[')
            map2[i].append(']')
        elif map[i][j] == '@':
            map2[i].append('@')
            map2[i].append('.')

roboti = 0
robotj = 0
for i in range(0, len(map)):
    for j in range(0, len(map[i])):
        if map[i][j] == '@':
            roboti = i
            robotj = j

for i in range(0, len(instructions)):
    instruction = instructions[i]
    if instruction == '^':
        # find the first empty space
        starti = roboti - 1
        while (starti > 0) and map[starti][robotj] == 'O':
            starti -= 1
        # move the blocks if possible
        if (starti > 0) and map[starti][robotj] == '.':
            roboti = roboti - 1
    elif instruction == 'v':
        # find the first empty space
        starti = roboti + 1
        while (starti <= len(map)) and map[starti][robotj] == 'O':
            starti += 1
        # move the blocks if possible
        if (starti <= len(map)) and map[starti][robotj] == '.':
            map[starti] = map[starti][:robotj] + 'O' + map[starti][robotj+1:]
            map[roboti + 1] = map[roboti + 1][:robotj] + '@' + map[roboti + 1][robotj+1:]
            map[roboti] = map[roboti][:robotj] + '.' + map[roboti][robotj+1:]
            roboti = roboti + 1
    elif instruction == '<':
        # find the first empty space
        startj = robotj - 1
        while (startj > 0) and map[roboti][startj] == 'O':
            startj -= 1
        # move the blocks if possible
        if (startj > 0) and map[roboti][startj] == '.':
            map[roboti] = map[roboti][:startj] + 'O' + map[roboti][startj + 1:]
            map[roboti] = map[roboti][:robotj - 1] + '@' + map[roboti][robotj:]
            map[roboti] = map[roboti][:robotj] + '.' + map[roboti][robotj+1:]
            robotj = robotj - 1
    elif instruction == '>':
        # find the first empty space
        startj = robotj + 1
        while (startj <= len(map)) and map[roboti][startj] == 'O':
            startj += 1
        # move the blocks if possible
        if (startj <= len(map)) and map[roboti][startj] == '.':
            map[roboti] = map[roboti][:startj] + 'O' + map[roboti][startj + 1:]
            map[roboti] = map[roboti][:robotj + 1] + '@' + map[roboti][robotj + 2:]
            map[roboti] = map[roboti][:robotj] + '.' + map[roboti][robotj+1:]
            robotj = robotj + 1

gps = 0
for i in range(0, len(map)):
    for j in range(0, len(map[i])):
        if map[i][j] == 'O':
            gps += 100 * i + j
print(gps)
