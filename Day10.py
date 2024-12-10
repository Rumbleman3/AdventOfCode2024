
# Set up
import re
import copy
map = []
with open('Day10.input', 'r') as file:
    for line in file:
        line = line.replace('\n','')
        map.append(line)

# Silver star
trailsum = 0   
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for i in range(len(map)):
    for j in range(len(map[i])):        
        if int(map[i][j]) == 0:      
            stops = []   
            stops.append([0, i, j])
            summits = []
            while len(stops) != 0:
                stop = stops.pop()
                for direction in directions:
                    newi = stop[1] + direction[0]
                    newj = stop[2] + direction[1]
                    if newi >= 0 and newi < len(map) and newj >=0 and newj < len(map[i]):
                        newstop = int(map[newi][newj])
                        if newstop == stop[0] + 1:
                            if newstop == 9:
                                summit = [newi, newj]
                                if summit not in summits:
                                    summits.append(summit)
                            else:
                                stops.append([newstop, newi, newj])
            trailsum += len(summits)
print(trailsum)                    

# Gold star
ratingsum = 0   
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for i in range(len(map)):
    for j in range(len(map[i])):        
        if int(map[i][j]) == 0:      
            stops = []
            stops.append([[0, i, j]])
            summits = []
            while len(stops) != 0:
                stop = stops.pop()
                for direction in directions:
                    newi = stop[len(stop) - 1][1] + direction[0]
                    newj = stop[len(stop) - 1][2] + direction[1]
                    if newi >= 0 and newi < len(map) and newj >=0 and newj < len(map[i]):
                        newstop = int(map[newi][newj])
                        if newstop == stop[len(stop) - 1][0] + 1:
                            if newstop == 9:
                                summit = copy.deepcopy(stop)
                                summit.append([newstop, newi, newj])
                                if summit not in summits:
                                    summits.append(summit)
                            else:
                                newStop = copy.deepcopy(stop)
                                newStop.append([newstop, newi, newj])
                                stops.append(newStop)
            ratingsum += len(summits)
print(ratingsum)   
