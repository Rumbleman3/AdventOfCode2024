# Setup
map = []
with open('Day16.input', 'r') as file:
    for line in file:
        line = line.replace('\n','')
        map.append(line)

# silver star
weightedmap = []
for i in range(0, len(map)):
    row = []
    for j in range(0, len(map[i])):
        row.append(-1)
    weightedmap.append(row)

# find S
starti = 0
startj = 0
for i in range(0, len(map)):
    for j in range(1, len(map)):
        if map[i][j] == 'S':
            starti = i
            startj = j

import copy
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
routes = [[[starti, startj, [0, 1], 0]]]
completedroutes = []
while len(routes) > 0:
    lowestRoute = -1
    lowestIndex = -1
    for index in range(0, len(routes)):
        route = routes[index]
        routePoint =  route[len(route) - 1][3]
        if lowestRoute == -1 or lowestRoute > routePoint:
            lowestRoute = routePoint
            lowestIndex = index
    route = routes.pop(lowestIndex)
    i = route[len(route) - 1][0]
    j = route[len(route) - 1][1]    
    facing = route[len(route) - 1][2]
    score = route[len(route) - 1][3]
    
    for direction in directions:        
        newi = i + direction[0]
        newj = j + direction[1]  
        newfacing = direction
        newscore = score + 1
        if newfacing != facing:
            newscore += 1000
        if map[newi][newj] == '.':        
            if weightedmap[newi][newj] == -1 or weightedmap[newi][newj] > newscore:
                weightedmap[newi][newj] = newscore
            else:
                continue
            if len(route) == 1 or (route[len(route) - 2][0] != newi or route[len(route) - 2][1] != newj):
                newroute = copy.deepcopy(route)
                newroute.append([newi, newj, newfacing, newscore])
                routes.append(newroute)
        elif map[newi][newj] == 'E':
            newroute = copy.deepcopy(route)
            newroute.append([newi, newj, newfacing, newscore])
            completedroutes.append(newroute)

lowestscore = 0
for route in completedroutes:
    if lowestscore == 0 or lowestscore > route[len(route) - 1][3]:
        lowestscore = route[len(route) - 1][3]
print(lowestscore)

