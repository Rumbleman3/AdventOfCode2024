# Setup
file = open("day11.input", "r")
line = file.read()
file.close()
stones = line.split()
stones = list(map(int, stones))

# silver brute force
for i in range(0, 25):
    newStones = []
    for stone in stones:
        num = int(stone)
        if num == 0:
            newStones.append('1')
        elif len(stone) % 2 == 0:
            midpoint = len(stone) // 2            
            newStone1 = int(stone[:midpoint])
            newStone2 = int(stone[midpoint:])
            newStones.append(str(newStone1))
            newStones.append(str(newStone2))
        else:
            newStones.append(str(num * 2024))
    stones = newStones
print(len(newStones))

# get the initial map ready
import copy
initialmap = {}
queue = [0]
while len(queue) > 0:
    stone = queue.pop()
    if stone not in initialmap:  
        newStones = [stone]
        index = 0
        while index < len(newStones):
            newstone = newStones[index]
            if newstone == 0:
                newStones[index] = 1
            elif len(str(newstone)) % 2 == 0:
                stonechar = str(newstone)
                midpoint = len(stonechar) // 2            
                newStone1 = int(stonechar[:midpoint])
                newStone2 = int(stonechar[midpoint:])
                newStones[index] = newStone1
                index += 1
                newStones.insert(index, newStone2)
            else:
                newStones[index] = newstone * 2024
            index += 1
        newnewnewStones = {}
        for j in newStones:
            if j not in newnewnewStones:
                newnewnewStones[j] = 1
            else:
                newnewnewStones[j] += 1
        initialmap[stone] = newnewnewStones
        for newstone in newStones:
            if newstone not in queue:
                queue.append(newstone)

# expand the map to 75 level
finalmap = {}
for index, (key, value) in enumerate(initialmap.items()):
    finalmap[key] = []
    finalmap[key].append(value)
    nextElement = value
    for i in range(1, 75):
        nextElement2 = {}
        for index2, (key2, value2) in enumerate(nextElement.items()):
            itemStone = key2
            itemCount = value2
            for index3, (key3, value3) in enumerate(initialmap[itemStone].items()):
                if key3 not in nextElement2:
                    nextElement2[key3] = value3 * itemCount
                else:
                    nextElement2[key3] += value3 * itemCount
        nextElement = copy.deepcopy(nextElement2)
        finalmap[key].append(nextElement)

# print out 
finalvalue = 0
for index5, (key5, value5) in enumerate(finalmap[0][21].items()):
    finalvalue += value5
print(finalvalue)

# Gold star
count = 0
test2 = stones
for stone in test2:
    count += 1
    remaining = 75
    queue = [stone]
    while remaining > 0:
        queue4 = []
        while len(queue) > 0:
            stone2 = queue.pop()
            if stone2 in finalmap:
                for index5, (key5, value5) in enumerate(finalmap[stone2][remaining - 1].items()):
                    count += value5
                count -= 1
            else:
                if stone2 == 0:
                    queue4.append(1)
                elif len(str(stone2)) % 2 == 0:
                    stonechar = str(stone2)
                    midpoint = len(stonechar) // 2   
                    newStone1 = int(stonechar[:midpoint])
                    newStone2 = int(stonechar[midpoint:])
                    queue4.append(newStone1)
                    queue4.append(newStone2)
                    count += 1
                else:
                    queue4.append(stone2 * 2024)

        queue = copy.deepcopy(queue4)                
        remaining -= 1
print(count)


