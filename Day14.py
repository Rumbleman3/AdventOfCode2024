# Set up
import re
robots = []
with open('Day14.input', 'r') as file:
    for line in file:
        line = re.findall(r'-?\d+', line)
        robots.append(line)

# silver
q1 = []
q2 = []
q3 = []
q4 = []
seconds = 100
length = 101
height = 103
for robot in robots:
    x = (int(robot[0]) + seconds * int(robot[2])) % length
    y = (int(robot[1]) + seconds * int(robot[3])) % height
    middlex = int(length / 2)
    middley = int(height / 2)
    if (x < middlex) and (y < middley):
        q1.append([x, y])
    elif (x > middlex) and (y < middley):
        q2.append([x, y])
    elif (x < middlex) and (y > middley):
        q3.append([x, y])
    elif (x > middlex) and (y > middley):
        q4.append([x, y])
total = len(q1) * len(q2) * len(q3) * len(q4)
print(total)

# gold
found = False
second = 1
empty_map = []
for i in range(0, 103):
    empty_map.append([])
    for j in range(0, 101):
        empty_map[i].append('.')
import copy
while not found:
    map = copy.deepcopy(empty_map)
    for robot in robots:        
        x = (int(robot[0]) + second * int(robot[2])) % length
        y = (int(robot[1]) + second * int(robot[3])) % height
        map[y][x] = '1'
    
    linedup = False
    for i in range (50, 103):
        for j in range (0, 101):
            if map[i][j] == '1':
                for index in range(0, 11):
                    if i + index < 103:
                        if map[i + index][j] != '1':
                            break
                    else:
                        break
                if index == 10:
                    linedup = True
            if linedup:
                break
        if linedup:
            break
    if linedup:
        break

    second += 1

print(second)
for line in map:
    print(line)
        
#     starti = 0
#     startj = 0
#     for i in range (0, 103):
#         for j in range (0, 101):
#             if map[i][j] == '1':
#                 starti = i
#                 startj = j
    
#     found = True
#     currenti = starti
#     currentj = startj
#     while found:        
#         found = False
#         for m in range (-1, 1):
#             for n in range (-1, 1): 
#                 nexti = currenti + m
#                 nextj = currentj + n
#                 if nexti >= 0 and nexti < 103 and nextj >= 0 and nextj < 103:
#                     if map[nexti][nextj] == '1':
#                         currenti = nexti
#                         currentj = nextj
#                         found = True
#                         continue
#         if nexti == starti and nextj == startj:
#             break
        
#     if found:
#         for i in range(0, 103):
#             line = ''
#             for j in range(0, 101):
#                 line += str(map[i][j])
#             print(line + '\n')
    