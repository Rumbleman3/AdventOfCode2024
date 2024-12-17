# Setup
A = 0
B = 0
C = 0
Program = []

import re
with open('Day17.input', 'r') as file:
    for line in file:
        if line.startswith("Register A: "):
            A = int(re.findall(r'\d+', line)[0])
        elif line.startswith("Register B: "):
            B = int(re.findall(r'\d+', line)[0])
        elif line.startswith("Register C: "):
            C = int(re.findall(r'\d+', line)[0])
        elif line.startswith("Program: "):
            Program = re.findall(r'-?\d+', line)
            Program = [int(number) for number in Program]

# silver
instructionIndex = 0
while instructionIndex < len(Program):
    operand = Program[instructionIndex + 1]
    literalOperand = operand
    comboOperand = operand
    if operand == 4:
        comboOperand = A
    elif operand == 5:
        comboOperand = B
    elif operand == 6:
        comboOperand = C

    opcode = Program[instructionIndex]
    if opcode == 0:
        A = int(A / (2 ** comboOperand))
    elif opcode == 1:
        B = int(B ^ literalOperand)
    elif opcode == 2:
        B = int(comboOperand % 8)
    elif opcode == 3:
        if A != 0:
            instructionIndex = literalOperand
            continue
    elif opcode == 4:
        B = int(B ^ C)
    elif opcode == 5:
        print(comboOperand % 8, end=',')
    elif opcode == 6:
        B = int(A / (2 ** comboOperand))
    elif opcode == 7:
        C = int(A / (2 ** comboOperand))
    instructionIndex += 2

# Gold
startSet = [192, 196, 198, 199, 200, 249]
currentSet = startSet
currentLevel = 3
nextSet = []
while True:
    currentLevel += 1
    for number in currentSet:
        nextStart = number << 3
        valueA = nextStart
        while valueA < nextStart + 8:
            output = []
            A = valueA
            instructionIndex = 0
            while instructionIndex < len(Program):
                operand = Program[instructionIndex + 1]
                literalOperand = operand
                comboOperand = operand
                if operand == 4:
                    comboOperand = A
                elif operand == 5:
                    comboOperand = B
                elif operand == 6:
                    comboOperand = C

                opcode = Program[instructionIndex]
                if opcode == 0:
                    A = int(A / (2 ** comboOperand))
                elif opcode == 1:
                    B = int(B ^ literalOperand)
                elif opcode == 2:
                    B = int(comboOperand % 8)
                elif opcode == 3:
                    if A != 0:
                        instructionIndex = literalOperand
                        continue
                elif opcode == 4:
                    B = int(B ^ C)
                elif opcode == 5:
                    output.append(comboOperand % 8)
                elif opcode == 6:
                    B = int(A / (2 ** comboOperand))
                elif opcode == 7:
                    C = int(A / (2 ** comboOperand))
                instructionIndex += 2

            levelsRemainingToCheck = currentLevel
            for outputIndex in range(len(output)-1, len(output)-1-currentLevel, -1):
                outputNumber = output[outputIndex]
                programNumber = Program[len(Program)-1-(currentLevel-levelsRemainingToCheck)]
                if outputNumber == programNumber:
                    levelsRemainingToCheck -= 1
                else:
                    break
            if levelsRemainingToCheck == 0:
                nextSet.append(valueA)
            if output == Program:
                break
            valueA += 1
        if output == Program:
            break
    if output == Program:
        break
    currentSet = nextSet
    nextSet = []
print(valueA)
            