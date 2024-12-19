# Set up
stripes = []
towels = []
with open('Day19.input', 'r') as file:
    lines = file.readlines()

readingStripes = True
stripesline = ''
for lineNum, line in enumerate(lines):
    if readingStripes:
        if lines[lineNum] != '\n':
            stripesline += lines[lineNum]
        else:
            stripes = stripesline.strip('\n').split(', ')
            readingStripes = False
    else:
        towels.append(lines[lineNum].strip('\n'))

# Silver star
possible = []
for towel in towels:
    queue = [[towel, towel]]
    while len(queue) > 0:
        remainingTowel = queue.pop()
        for stripe in stripes:
            if remainingTowel[0].startswith(stripe):
                piece = remainingTowel[0][len(stripe):]
                if len(piece) == 0 and remainingTowel[1] not in possible:
                    possible.append(towel)
                    queue = list(filter(lambda x: x[1] not in towel, queue))
                    break
                else:
                    queue.append([piece, towel])
print(len(possible))

# Gold star
possible = 0
hashedStripes = {}
for stripe in stripes:
    head = stripe[0]
    if head in hashedStripes:
        hashedStripes[head].append(stripe)
    else:
        hashedStripes[head] = [stripe]

for towel in towels:
    queue = [[towel, towel, 1]]
    while len(queue) > 0:
        remainingTowel = queue.pop(0)
        # for stripe in stripes:
        values = hashedStripes[remainingTowel[0][0]]
        for stripe in values:
            if remainingTowel[0].startswith(stripe):
                piece = remainingTowel[0][len(stripe):]
                if len(piece) == 0:
                    possible += remainingTowel[2]
                else:
                    addtoqueue = True
                    for candidate in queue:
                        if piece == candidate[0]:
                            candidate[2] += remainingTowel[2]
                            addtoqueue = False
                            break
                    if addtoqueue:
                        queue.append([piece, towel, remainingTowel[2]])

print(possible)

