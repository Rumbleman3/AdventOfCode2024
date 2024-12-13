# Set up
import re
with open('Day13.input', 'r') as file:
    content = file.read()

lines = content.splitlines()

lineIndex = 0
claws = []
while lineIndex < len(lines):
    buttonA = re.findall(r'\b\d+\b', lines[lineIndex])
    lineIndex += 1
    buttonB = re.findall(r'\b\d+\b', lines[lineIndex])
    lineIndex += 1
    target = re.findall(r'\b\d+\b', lines[lineIndex])
    lineIndex += 2
    claws.append([buttonA, buttonB, target])

# silver star
totalTokens = 0
for index, item in enumerate(claws):
    ax = int(item[0][0])
    ay = int(item[0][1])
    bx = int(item[1][0])
    by = int(item[1][1])
    prizex = int(item[2][0])
    prizey = int(item[2][1])
    limitAX = int(prizex / ax) + 1 
    limitAY = int(prizey / ay) + 1 
    limitBX = int(prizex / bx) + 1 
    limitBY = int(prizey / by) + 1 
    limitA = limitAX
    if limitAX > limitAY:
        limitA = limitAY
    if limitA > 100:
        limitA = 100
    limitB = limitBX
    if limitBX > limitBY:
        limitB = limitBY
    if limitB > 100:
        limit = 100
    tokenHit = []
    for i in range(1, limitA):
        for j in range(1, limitB):
            x = i * ax + j * bx
            y = i * ay + j * by
            if x == prizex and y == prizey and i <= 100 and j <= 100:
                tokenHit.append(i * 3 + j)
    
    smallestToken = -1
    for token in tokenHit:
        if smallestToken == -1 or token < smallestToken:
            smallestToken = token

    if (smallestToken != -1):
        totalTokens += smallestToken
print(totalTokens)

# gold star
from sympy import symbols, Eq, solve
from fractions import Fraction
#claws = [[['94','34'],['22','67'],['8400','5400']],[['26','66'],['67','21'],['12748','12176']],[['17','86'],['84','37'],['7870','6450']],[['69','23'],['27','71'],['18641','10279']]]
totalTokens = 0
for index, item in enumerate(claws):
    ax = int(item[0][0])
    ay = int(item[0][1])
    bx = int(item[1][0])
    by = int(item[1][1])
    prizex = int(item[2][0]) + 10000000000000
    prizey = int(item[2][1]) + 10000000000000
    limitAX = int(prizex / ax) + 1 
    limitAY = int(prizey / ay) + 1 
    limitBX = int(prizex / bx) + 1 
    limitBY = int(prizey / by) + 1 
    limitA = limitAX
    if limitAX > limitAY:
        limitA = limitAY
    limitB = limitBX
    if limitBX > limitBY:
        limitB = limitBY
    tokenHit = []    
    i, j = symbols('i j')
    equation1 = Eq(ax * i + bx * j, prizex)
    equation2 = Eq(ay * i + by * j, prizey)
    solution = solve((equation1, equation2), (i, j))

    i = solution[i]
    j = solution[j]
    if i.is_integer and j.is_integer:
        totalTokens += (i * 3 + j)
print(totalTokens)

