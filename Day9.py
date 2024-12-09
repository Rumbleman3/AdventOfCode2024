import copy

# Set up
file = open("day9.input", "r")
diskmap = file.read()
file.close()

fileIndex = 0
expanded = ''
for index, char in enumerate(diskmap):
    if index % 2 == 0:
        expanded = expanded + (chr(fileIndex) * int(char))
        fileIndex += 1
    else:
        expanded = expanded + (chr(20000) * int(char))

# Silver star
# compactOriginal = list(copy.deepcopy(expanded))
# compact = list(copy.deepcopy(expanded))
# open = 0
# for i in range(len(expanded) - 1, 0, -1):
#     while (compact[open] != chr(20000)):
#         open += 1
#     if (open > i):
#         break
#     compact[open] = expanded[i]     
#     compact[i] = chr(20000)

# checksum = 0
# for index in range(0, i + 1):
#     number = ord(compact[index])
#     checksum += index * number
#     if index == 49780:
#         continue
# print(checksum)
           
# Gold star
compactOriginal = list(copy.deepcopy(expanded))
compact = list(copy.deepcopy(expanded))
openSlots = []
openStart = -1
for index, character in enumerate(compact):
    if (character == chr(20000)) and openStart == -1:
        openStart = index
    elif (character == chr(20000)):
        continue
    elif openStart != -1:
        openSlots.append([openStart, index - openStart])
        openStart = -1

current = len(compact)
moveEnd = -1
moveChar = chr(20001)
lastMoveChar = chr(20001)
while current >= 0:
    current -= 1
    if current <= openSlots[0][0]:
        break

    if moveEnd == -1:
        if (compact[current] == chr(20000)):
            continue
        else:
            moveEnd = current
            moveChar = compact[current]
    else:
        if (compact[current] == chr(20000)):
            if ord(moveChar) < ord(lastMoveChar):
                length = moveEnd - current
                for slot in openSlots:
                    if slot[0] > current:
                        break
                    if slot[1] >= length:
                        for fillIndex in range(slot[0], slot[0] + length):
                            compact[fillIndex] = moveChar
                        for fillIndex in range(current + 1, moveEnd + 1):
                            compact[fillIndex] = chr(20000)     
                            if fillIndex == 38178 or fillIndex == 38179:
                                a = 1
                        if (length == slot[1]):
                            openSlots.remove(slot)
                        else:
                            slot[0] = slot[0] + length
                            slot[1] = slot[1] - length    
                        break
                lastMoveChar = moveChar
            moveEnd = -1
            moveChar = chr(20001)
        elif (compact[current] != moveChar):  
            if ord(moveChar) < ord(lastMoveChar):          
                length = moveEnd - current
                for slot in openSlots:
                    if slot[0] > current:
                        break
                    if slot[1] >= length:
                        for fillIndex in range(slot[0], slot[0] + length):
                            compact[fillIndex] = moveChar
                        for fillIndex in range(current + 1, moveEnd + 1):
                            compact[fillIndex] = chr(20000)     
                            if fillIndex == 38178 or fillIndex == 38179:
                                a = 1
                        if (length == slot[1]):
                            openSlots.remove(slot)
                        else:
                            slot[0] = slot[0] + length
                            slot[1] = slot[1] - length
                        break
                lastMoveChar = moveChar
            moveEnd = current
            moveChar = compact[current]

checksum = 0
for index in range(0, len(compact) - 1):
    if (compact[index] != chr(20000)):
        number = ord(compact[index])
        checksum += index * number
print(checksum)

