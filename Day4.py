
# Setup
array = []
with open('Day4.input', 'r') as file:
    for line in file:
        array.append(line)

# Silver star
XMAS = 0
for currentY, line in enumerate(array):
    for currentX, char in enumerate(line):
        if char == 'X':
            direction = [-1, 0, 1]
            for x in direction:
                for y in direction:
                    indexX = currentX + x
                    indexY = currentY + y
                    if indexX < 0 or indexX >= len(line) or indexY < 0 or indexY >= len(array) or array[indexY][indexX] != 'M':
                        continue 
                    indexX += x
                    indexY += y
                    if indexX < 0 or indexX >= len(line) or indexY < 0 or indexY >= len(array) or array[indexY][indexX] != 'A':
                        continue 
                    indexX += x
                    indexY += y
                    if indexX < 0 or indexX >= len(line) or indexY < 0 or indexY >= len(array) or array[indexY][indexX] != 'S':
                        continue 
                    XMAS += 1
print(XMAS)

# Gold star
XMAS = 0
for currentY, line in enumerate(array):
    for currentX, char in enumerate(line):
        if char == 'A':
            direction = [-1, 1]
            found = False
            for x in direction:
                for y in direction:
                    indexX = currentX + x
                    indexY = currentY + y
                    if indexX < 0 or indexX >= len(line) or indexY < 0 or indexY >= len(array) or array[indexY][indexX] != 'M':
                        continue 
                    indexX = currentX - x
                    indexY = currentY - y
                    if indexX < 0 or indexX >= len(line) or indexY < 0 or indexY >= len(array) or array[indexY][indexX] != 'S':
                        continue 
                    indexX = currentX - x
                    indexY = currentY + y
                    if indexX < 0 or indexX >= len(line) or indexY < 0 or indexY >= len(array) or (array[indexY][indexX] != 'M' and array[indexY][indexX] != 'S'):
                        continue 
                    isM = array[indexY][indexX] == 'M'
                    indexX = currentX + x
                    indexY = currentY - y
                    if indexX < 0 or indexX >= len(line) or indexY < 0 or indexY >= len(array) or (isM and array[indexY][indexX] != 'S') or (not isM and array[indexY][indexX] != 'M'):
                        continue 
                    XMAS += 1
                    found = True
                    break
                if (found):
                    break
print(XMAS)
