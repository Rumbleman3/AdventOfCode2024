# set up
import re
codes = []
with open('Day21.input', 'r') as file:
    for line in file:
        line = line.strip('\n')
        codes.append(line)

numPad = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], [' ', '0', 'A']]
dirPad = [[' ', '^', 'A'], ['<', 'v', '>']]

numHash = {}
for i in range(0, len(numPad)):
    for j in range(0, len(numPad[i])):
        numHash[numPad[i][j]] = [i, j]
dirHash = {}
for i in range(0, len(dirPad)):
    for j in range(0, len(dirPad[i])):
        button = dirPad[i][j]
        if button == '^':
            dirHash[dirPad[i][j]] = [[i, j],[-1, 0]]
        elif button == 'A':
            dirHash[dirPad[i][j]] = [[i, j],[0, 0]]
        elif button == '<':
            dirHash[dirPad[i][j]] = [[i, j],[0, -1]]
        elif button == 'v':
            dirHash[dirPad[i][j]] = [[i, j],[1, 0]]
        elif button == '>':
            dirHash[dirPad[i][j]] = [[i, j],[0, 1]]

import itertools
import copy
def getdirectionsfromdirectionpair(currentDirectionCodes):
    finalPaths = []
    fewestchanges = -1
    pos = dirHash[currentDirectionCodes[0]][0]
    paths = []
    currentPaths = []
    dest = dirHash[currentDirectionCodes[1]]
    idiff = dest[0][0] - pos[0]
    jdiff = dest[0][1] - pos[1]
    for index in range(0, abs(idiff)):
        if idiff > 0:
            currentPaths.append([1, 0])
        else:
            currentPaths.append([-1, 0])
    for index in range(0, abs(jdiff)):
        if jdiff > 0:
            currentPaths.append([0, 1])
        else:                
            currentPaths.append([0, -1])
    currentPaths = list(itertools.permutations(currentPaths))   
    currentPathsdeduped = []
    for element in currentPaths:
        element = list(element)
        currentcheckpos = copy.deepcopy(pos)
        invalid = False
        for elementstop in element:
            currentcheckpos[0] += elementstop[0]
            currentcheckpos[1] += elementstop[1]
            if currentcheckpos == [0, 0]:
                invalid = True
                break
        if not invalid:
            element.append([0,0])
            if element not in currentPathsdeduped:
                currentPathsdeduped.append(element)
    paths.append(currentPathsdeduped)
    pos = dest[0]
    paths = list(itertools.product(*paths))
    for path in paths: 
        flattened = [item for sublist in path for item in sublist] 
        curpos = [0,2]
        changes = 0   
        for index in range(0, len(flattened)):
            for key, value in dirHash.items():
                if value[1] == flattened[index]:
                    nextpos = value[0]
                    break
            distance = abs(curpos[0] - nextpos[0]) + abs(curpos[1] - nextpos[1])
            changes += distance
            curpos = nextpos
        if fewestchanges == -1 or fewestchanges > changes: 
            fewestchanges = changes
        finalPaths.append([flattened, changes])

    finalPaths = list(filter(lambda x: x[1] <= fewestchanges, finalPaths))
    return finalPaths

def getdirectionsfromdirections(currentDirectionCodes):
    finalPaths = []
    fewestchanges = -1
    for currentDirectionCode in currentDirectionCodes:
        pos = [0, 2]
        paths = []
        for char in currentDirectionCode:
            currentPaths = []
            dest = dirHash[char]
            idiff = dest[0][0] - pos[0]
            jdiff = dest[0][1] - pos[1]
            for index in range(0, abs(idiff)):
                if idiff > 0:
                    currentPaths.append([1, 0])
                else:
                    currentPaths.append([-1, 0])
            for index in range(0, abs(jdiff)):
                if jdiff > 0:
                    currentPaths.append([0, 1])
                else:                
                    currentPaths.append([0, -1])
            currentPaths = list(itertools.permutations(currentPaths))   
            currentPathsdeduped = []
            for element in currentPaths:
                element = list(element)
                currentcheckpos = copy.deepcopy(pos)
                invalid = False
                for elementstop in element:
                    currentcheckpos[0] += elementstop[0]
                    currentcheckpos[1] += elementstop[1]
                    if currentcheckpos == [0, 0]:
                        invalid = True
                if not invalid:
                    element.append([0,0])
                    if element not in currentPathsdeduped:
                        currentPathsdeduped.append(element)
            paths.append(currentPathsdeduped)
            pos = dest[0]
        paths = list(itertools.product(*paths))
        for path in paths: 
            flattened = [item for sublist in path for item in sublist] 
            curpos = [0,2]
            changes = 0   
            for index in range(0, len(flattened)):
                for key, value in dirHash.items():
                    if value[1] == flattened[index]:
                        nextpos = value[0]
                        break
                distance = abs(curpos[0] - nextpos[0]) + abs(curpos[1] - nextpos[1])
                changes += distance
                curpos = nextpos
            if fewestchanges == -1 or fewestchanges > changes:
                fewestchanges = changes
            finalPaths.append([flattened, changes])

    finalPaths = list(filter(lambda x: x[1] <= fewestchanges, finalPaths))
    return finalPaths

def getcodes(directions):
    directioncodes = []
    for direction in directions:
        directioncode = []
        for stop in direction[0]:
            for key, value in dirHash.items():
                if value[1] == stop:
                    directioncode.append(key)
        directioncodes.append(directioncode)
    return directioncodes

def getdirectionsfromnum(code):
    paths = []
    pos = [3, 2]
    for char in code:
        currentPaths = []
        dest = numHash[char]
        idiff = dest[0] - pos[0]
        jdiff = dest[1] - pos[1]
        for index in range(0, abs(idiff)):
            if idiff > 0:
                currentPaths.append([1, 0])
            else:
                currentPaths.append([-1, 0])
        for index in range(0, abs(jdiff)):
            if jdiff > 0:
                currentPaths.append([0, 1])
            else:                
                currentPaths.append([0, -1])
        currentPaths = list(itertools.permutations(currentPaths))   
        currentPathsdeduped = []
        for element in currentPaths:
            element = list(element)
            currentcheckpos = copy.deepcopy(pos)
            invalid = False
            for elementstop in element:
                currentcheckpos[0] += elementstop[0]
                currentcheckpos[1] += elementstop[1]
                if currentcheckpos == [3, 0]:
                    invalid = True
            if not invalid:
                element.append([0,0])
                if element not in currentPathsdeduped:
                    currentPathsdeduped.append(element)
        paths.append(currentPathsdeduped)
        pos = dest
    paths = list(itertools.product(*paths))
    finalPaths = []
    fewestchanges = -1
    for path in paths:
        flattened = [item for sublist in path for item in sublist]     
        curpos = [0,2]
        changes = 0   
        for index in range(0, len(flattened)):
            for key, value in dirHash.items():
                if value[1] == flattened[index]:
                    nextpos = value[0]
                    break
            distance = abs(curpos[0] - nextpos[0]) + abs(curpos[1] - nextpos[1])
            changes += distance
            curpos = nextpos
        if fewestchanges == -1 or fewestchanges > changes:
            fewestchanges = changes
        finalPaths.append([flattened, changes])
    finalPaths = list(filter(lambda x: x[1] <= fewestchanges, finalPaths))
    return finalPaths

possibledirectionchanges = \
    [['A','^'],['A','>'],['A','v'],['A','<'] \
    ,['^','A'],['^','>'],['^','v'],['^','<'] \
    ,['>','^'],['>','A'],['>','v'],['>','<'] \
    ,['<','^'],['<','>'],['<','v'],['<','A'] \
    ,['v','^'],['v','>'],['v','A'],['v','<']]
basicmovesneeded = []
movesneeded = []
for change in possibledirectionchanges:
    directionchangescurrent = getdirectionsfromdirectionpair(change)
    directioncodescurrent = getcodes(directionchangescurrent)
    for index in range(0, 1):
        directionchangescurrent = getdirectionsfromdirections(directioncodescurrent)
        directioncodescurrent = getcodes(directionchangescurrent)
    movesneeded.append([change, len(directioncodescurrent[0])])
    
# silver
finalComplexity = 0
for code in codes:    
    directions1 = getdirectionsfromnum(code)
    directioncodes1 = getcodes(directions1)
    min_length = min(len(sub_array) for sub_array in directioncodes1)
    directioncodes1 = [sub_array for sub_array in directioncodes1 if len(sub_array) == min_length]
    currentpos = 'A'
    lowestrunsteps = -1
    for run in directioncodes1:
        runsteps = 0
        for step in run:
            nextpos = step
            if currentpos == nextpos:
                runsteps += 1
            else:
                for move in movesneeded:
                    if [currentpos, nextpos] == move[0]:
                        runsteps += move[1]
            currentpos = nextpos
        if lowestrunsteps == -1 or lowestrunsteps > runsteps:
            lowestrunsteps = runsteps
    finalComplexity += lowestrunsteps * int(code.strip('A'))
print(finalComplexity)


      