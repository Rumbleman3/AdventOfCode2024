# set up
import re
steps = []
with open('Day18.input', 'r') as file:
    for line in file:
        step = re.findall(r'-?\d+', line)
        step = [int(number) for number in step]
        steps.append(step)

width = 71
height = 71
map = []
for i in range(0, height):
    row = []
    for j in range(0, width):
        row.append('.')
    map.append(row)

# silver and gold star
for index in range(0, 2852):
    i = steps[index][1]
    j = steps[index][0]
    map[i][j] = '#'
    
weightedmap = []
for i in range(0, len(map)):
    row = []
    for j in range(0, len(map[i])):
        row.append(-1)
    weightedmap.append(row)

import copy
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
routes = [[[0, 0, [0, 1], 0]]]
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
        if newi >= 0 and newj >= 0 and newi < height and newj < width and map[newi][newj] == '.':        
            if weightedmap[newi][newj] == -1 or weightedmap[newi][newj] > newscore:
                if newi == 70 and newj == 70:
                    newroute = copy.deepcopy(route)
                    newroute.append([newi, newj, newfacing, newscore])
                    completedroutes.append(newroute)
                    break
                else:
                    weightedmap[newi][newj] = newscore                
            else:
                continue
            if len(route) == 1 or (route[len(route) - 2][0] != newi or route[len(route) - 2][1] != newj):
                newroute = copy.deepcopy(route)
                newroute.append([newi, newj, newfacing, newscore])
                routes.append(newroute)

lowestscore = 0
bestPath = []
for route in completedroutes:
    if lowestscore == 0 or lowestscore > route[len(route) - 1][3]:
        lowestscore = route[len(route) - 1][3]
        bestPath = route
print(lowestscore)