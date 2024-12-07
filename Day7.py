# Setup
import re
equations = []
with open('Day7.input', 'r') as file:
    for line in file:
        numbers = re.findall(r'\d+', line)
        equations.append(numbers)

# Silver star
total = 0
for equation in equations:
    finalResult = int(equation[0])
    numOperations = len(equation) - 2
    totalOperations = 2 ** numOperations
    for i in range(0, totalOperations):
        result = int(equation[1])
        for j in range(2, len(equation)):
            if i % 2 == 0:
                result += int(equation[j])
            else:
                result *= int(equation[j])
            if result > finalResult:
                break
            i = int(i/2)
        if finalResult == result:
            total += finalResult
            break
print(total)

# Gold star
total = 0
for equation in equations:
    finalResult = int(equation[0])
    numOperations = len(equation) - 2
    totalOperations = 3 ** numOperations
    for i in range(0, totalOperations):
        result = int(equation[1])
        for j in range(2, len(equation)):
            if i % 3 == 0:
                result += int(equation[j])
            elif i % 3 == 1:
                result *= int(equation[j])
            elif i % 3 == 2:
                result = int(str(result) + str(equation[j]))
            if result > finalResult:
                break
            i = int(i/3)
        if finalResult == result:
            total += finalResult
            break
print(total)
