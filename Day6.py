import copy

# Setup
original = []
with open('Day6.input', 'r') as file:
    for line in file:
        line = line.replace('\n','')
        original.append(line)

# silver star
currenti = 0
currentj = 0
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
array = copy.deepcopy(original)
for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j] == '^':
            currenti = i
            currentj = j
direction = 0
while (currenti >= 0 and currenti < len(array) and currentj >= 0 and currentj < len(array[currenti])):
    nexti = currenti + directions[direction][0]
    nextj = currentj + directions[direction][1]
    if (nexti >= 0 and nexti < len(array) and nextj >= 0 and nextj < len(array[nexti])):
        if array[nexti][nextj] == '#':
            direction += 1
            direction = direction % 4
            updatedList = list(array[currenti])
            updatedList[currentj] = '+'     
            updated = ''.join(updatedList)   
            array[currenti] = updated
        else:
            updatedList = list(array[nexti])
            updatedList[nextj] = 'X'     
            updated = ''.join(updatedList)   
            array[nexti] = updated
            currenti = nexti
            currentj = nextj
    else:
        break
path = 0
for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j] == 'X' or array[i][j] == '^' or array[i][j] == '+':
            path += 1
print(path)

# gold star
looped = 0
for i in range(len(array)):
    for j in range(len(array[i])):  
        if array[i][j] == 'X' or array[i][j] == '^' or array[i][j] == '+':            
            newArray = copy.deepcopy(original)
            for findi in range(len(newArray)):
                for findj in range(len(newArray[findi])):
                    if newArray[findi][findj] == '^':
                        currenti = findi
                        currentj = findj
            direction = 0
            updatedList = list(newArray[i])
            updatedList[j] = '#'     
            updated = ''.join(updatedList)   
            newArray[i] = updated            
            obstacles = []
            numHit = 0
            while (currenti >= 0 and currenti < len(newArray) and currentj >= 0 and currentj < len(newArray[currenti])):
                nexti = currenti + directions[direction][0]
                nextj = currentj + directions[direction][1]
                if (nexti >= 0 and nexti < len(newArray) and nextj >= 0 and nextj < len(newArray[nexti])):
                    if newArray[nexti][nextj] == '#':
                        obstacle = [nexti, nextj]
                        if obstacle in obstacles:
                            numHit += 1
                            if numHit > 4:    
                                looped += 1                            
                                break
                        else:
                            obstacles.append(obstacle)
                            numHit = 1
                        direction += 1
                        direction = direction % 4
                        updatedList = list(newArray[currenti])
                        updatedList[currentj] = '+'     
                        updated = ''.join(updatedList)   
                        newArray[currenti] = updated
                    else:
                        updatedList = list(newArray[nexti])
                        updatedList[nextj] = 'X'     
                        updated = ''.join(updatedList)   
                        newArray[nexti] = updated
                        currenti = nexti
                        currentj = nextj
                else:
                    break
print(looped)


