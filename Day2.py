import re

# Silver star
safeReport = 0
with open('Day2.input', 'r') as file:
    for line in file:
        numbers = re.findall(r'\d+', line)
        numbers = [int(number) for number in numbers]
        safe = True
        for index, number in enumerate(numbers):
            if index == 0:
                continue

            if index == 1:
                if (numbers[index - 1] > numbers[index] and abs(numbers[index - 1] - numbers[index]) <= 3):
                    direction = -1
                    continue
                elif (numbers[index - 1] < numbers[index] and abs(numbers[index - 1] - numbers[index]) <= 3):
                    direction = 1
                    continue
                else:
                    safe = False
                    break

            if direction == -1: 
                if (numbers[index - 1] > numbers[index] and abs(numbers[index - 1] - numbers[index]) <= 3):
                    continue
                else:
                    safe = False
                    break
            
            if direction == 1: 
                if (numbers[index - 1] < numbers[index] and abs(numbers[index - 1] - numbers[index]) <= 3):
                    continue
                else:
                    safe = False
                    break

        if safe == True:
            safeReport += 1
print(safeReport)

# Silver star
safeReport = 0
with open('Day2.input', 'r') as file:
    for line in file:
        numbers0 = re.findall(r'\d+', line)
        numbers0 = [int(number) for number in numbers0]
        indexLen = len(numbers0) + 1
        for index in range(indexLen):
            numbers = numbers0.copy()
            if index != indexLen - 1:
                del numbers[index]
            safe = True
            direction = 0
            for index, number in enumerate(numbers):
                if index == 0:
                    continue

                if index == 1:
                    if (numbers[index - 1] > numbers[index] and abs(numbers[index - 1] - numbers[index]) <= 3):
                        direction = -1
                        continue
                    elif (numbers[index - 1] < numbers[index] and abs(numbers[index - 1] - numbers[index]) <= 3):
                        direction = 1
                        continue
                    else:
                        safe = False
                        break

                if direction == -1: 
                    if (numbers[index - 1] > numbers[index] and abs(numbers[index - 1] - numbers[index]) <= 3):
                        continue
                    else:
                        safe = False
                        break
                
                if direction == 1: 
                    if (numbers[index - 1] < numbers[index] and abs(numbers[index - 1] - numbers[index]) <= 3):
                        continue
                    else:
                        safe = False
                        break
            if safe == True:
                break

        if safe == True:
            safeReport += 1
print(safeReport)
