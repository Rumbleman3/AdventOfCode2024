# Setup
import re
import copy
map = []
with open('Day12.input', 'r') as file:
    for line in file:
        line = line.replace('\n','')
        map.append(line)

# separate into areas
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
farms = []
for i in range(len(map)):
    for j in range(len(map[i])):
        currentLetter = map[i][j]
        current = [i, j]

        # check to see if it is already in a farm
        inFarm = False
        for farm in farms:
            if current in farm:
                inFarm = True
                break
        if inFarm:
            continue

        # do the land walk
        newFarm = []
        newFarm.append([i, j])
        queue = []
        queue.append([i, j])
        while len(queue) > 0:
            land = queue.pop()
            for direction in directions:
                newi = land[0] + direction[0]
                newj = land[1] + direction[1]     
                if newi >= 0 and newi < len(map) and newj >=0 and newj < len(map[i]):           
                    if currentLetter == map[newi][newj]:
                        newland = [newi, newj]
                        if newland not in newFarm:
                            newFarm.append(newland)
                            queue.append(newland)
        farms.append(newFarm)

# Silver star
total = 0
for farm in farms:
    farmPerimeter = 0
    for land in farm:        
        for direction in directions:
            newi = land[0] + direction[0]
            newj = land[1] + direction[1]  
            newLand = [newi, newj]
            if newLand not in farm:
                farmPerimeter += 1
    total += farmPerimeter * len(farm)
print(total)

# Gold star
total = 0
for farm in farms:
    perimetersTop = []
    perimetersBottom = []
    perimetersLeft = []
    perimetersRight = []
    for land in farm:        
        for direction in directions:
            newi = land[0] + direction[0]
            newj = land[1] + direction[1]  
            newLand = [newi, newj]
            if newLand not in farm:
                fence = [land[0], land[1], direction]
                if direction == [-1, 0]:
                    perimetersTop.append(fence)
                if direction == [0, -1]:
                    perimetersLeft.append(fence)
                if direction == [1, 0]:
                    perimetersBottom.append(fence)
                if direction == [0, 1]:
                    perimetersRight.append(fence)
    perimetersTop = sorted(perimetersTop, key= lambda x: (x[0], x[1]))
    index = 0
    while index < len(perimetersTop):
        if (index + 1 >= len(perimetersTop)):
            break
        if perimetersTop[index][0] == perimetersTop[index + 1][0] and perimetersTop[index][1] == perimetersTop[index + 1][1] - 1:
            perimetersTop.remove(perimetersTop[index])
        else:
            index += 1
    perimetersLeft = sorted(perimetersLeft, key= lambda x: (x[1], x[0]))
    index = 0
    while index < len(perimetersLeft):
        if (index + 1 >= len(perimetersLeft)):
            break
        if perimetersLeft[index][1] == perimetersLeft[index + 1][1] and perimetersLeft[index][0] == perimetersLeft[index + 1][0] - 1:
            perimetersLeft.remove(perimetersLeft[index])
        else:
            index += 1
    perimetersBottom = sorted(perimetersBottom, key= lambda x: (x[0], x[1]))
    index = 0
    while index < len(perimetersBottom):
        if (index + 1 >= len(perimetersBottom)):
            break
        if perimetersBottom[index][0] == perimetersBottom[index + 1][0] and perimetersBottom[index][1] == perimetersBottom[index + 1][1] - 1:
            perimetersBottom.remove(perimetersBottom[index])
        else:
            index += 1
    perimetersRight = sorted(perimetersRight, key= lambda x: (x[1], x[0]))
    index = 0
    while index < len(perimetersRight):
        if (index + 1 >= len(perimetersRight)):
            break
        if perimetersRight[index][1] == perimetersRight[index + 1][1] and perimetersRight[index][0] == perimetersRight[index + 1][0] - 1:
            perimetersRight.remove(perimetersRight[index])
        else:
            index += 1

    total += (len(perimetersTop) + len(perimetersLeft) + len(perimetersBottom) + len(perimetersRight)) * len(farm)
print(total)