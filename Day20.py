# Setup
map = []
weightedmap = []
with open('Day20.input', 'r') as file:
    for line in file:
        row = []
        weightedrow = []
        line = line.replace('\n','')
        for j in range(0, len(line)):
            row.append(line[j])
            weightedrow.append(-1)
        map.append(row)
        weightedmap.append(weightedrow)

starti = 0
startj = 0
for i in range(0, len(map)):
    for j in range(0, len(map[i])):
        if map[i][j] == 'S':
            starti = i
            startj = j
weightedmap[starti][startj] = 0

import copy
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
racing = True
i = starti
j = startj
facing = [0, 1]
score = 0
while racing:
    for direction in directions:        
        newi = i + direction[0]
        newj = j + direction[1]  
        newfacing = direction
        newscore = score + 1
        if map[newi][newj] == '.':        
            if weightedmap[newi][newj] == -1:
                weightedmap[newi][newj] = newscore                
                i = newi
                j = newj
                facing = newfacing
                score = newscore
        elif map[newi][newj] == 'E':
            weightedmap[newi][newj] = newscore       
            score = newscore
            racing = False
            break
officialscore = score
print(officialscore)

# silver star
i = starti
j = startj
facing = [0, 1]
score = 0
cheatscores = []
racing = True
while racing:
    for direction in directions:        
        newi = i + direction[0]
        newj = j + direction[1]  
        newfacing = direction
        newscore = score + 1
        if map[newi][newj] == '.':        
            if weightedmap[newi][newj] == weightedmap[i][j] + 1:
                nexti = newi
                nextj = newj
                nextfacing = newfacing
                nextscore = newscore
        elif map[newi][newj] == '#':
            if newi == 0 or newj == 0 or newi == len(map) - 1 or newj == len(map[newi]) - 1:
                continue
            newi2 = newi + direction[0]
            newj2 = newj + direction[1]
            if weightedmap[newi2][newj2] == -1:
                continue
            cheatscore = officialscore - (weightedmap[newi2][newj2] - weightedmap[i][j]) + 2                
            cheatscores.append(cheatscore)
        elif map[newi][newj] == 'E':
            racing = False
            break
    i = nexti
    j = nextj
    facing = nextfacing
    score = nextscore

timesave = 2
cheatCount = 0
for cheatscore in cheatscores:
    if officialscore >= cheatscore + timesave:
        cheatCount += 1
print(cheatCount)

# gold star
cheatNum = 20
i = starti
j = startj
score = 0
cheatscores = []
for m in range(0, len(weightedmap)):
    for n in range(0, len(weightedmap[m])):
        if weightedmap[m][n] != -1:
            localcheatscores = []
            for o in range(-cheatNum, cheatNum + 1):
                for p in range(-cheatNum, cheatNum + 1):
                    if (o != 0 or p != 0) and (abs(o) + abs(p) <= cheatNum):
                        targeti = m + o
                        targetj = n + p
                        if targeti >= 0 and targetj >= 0 and targeti < len(weightedmap) and targetj < len(weightedmap[targeti]):
                            targetscore = weightedmap[targeti][targetj] 
                            currentscore = weightedmap[m][n]
                            if targetscore != -1 and targetscore > currentscore + abs(o) + abs(p):
                                cheatscore = officialscore - (targetscore - currentscore) + abs(o) + abs(p)     
                                localcheatscores.append(cheatscore)
            cheatscores = cheatscores + localcheatscores
cheatscores.sort()
timesave = 100
cheatCount = 0
for cheatscore in cheatscores:
    if officialscore >= cheatscore + timesave:
        cheatCount += 1
print(cheatCount)

            



