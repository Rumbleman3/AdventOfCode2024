# set up
import re
original_gates = {}
original_instructions = []
with open('Day24.input', 'r') as file:
    lines = file.readlines()

readingGates = True
for lineNum, line in enumerate(lines):
    if readingGates:
        if lines[lineNum] != '\n':
            match = re.match(r'(\w+\d{2}): (\d+)', lines[lineNum])
            original_gates[match[1]] = int(match[2])
        else:
            readingGates = False
    else:
        match = re.match(r'(\w+)\s(\w+)\s(\w+)\s->\s(\w+)', lines[lineNum])
        original_instructions.append([match[1], match[2], match[3], match[4]])

# silver
# import copy
# gates = copy.deepcopy(original_gates)
# instructions = copy.deepcopy(original_instructions)
# while len(instructions) > 0:
#     for instruction in instructions:
#         input0 = instruction[0]
#         input1 = instruction[2]
#         operand = instruction[1]
#         output = instruction[3]
#         if input0 in gates and input1 in gates:
#             if operand == 'AND':
#                 gates[output] = gates[input0] & gates[input1]
#             elif operand == 'OR':                
#                 gates[output] = gates[input0] | gates[input1]
#             elif operand == 'XOR':
#                 if gates[input0] == gates[input1]:
#                     gates[output] = 0
#                 else:
#                     gates[output] = 1
#             instructions.remove(instruction)
#             break
# gates = dict(sorted(gates.items()))
# gates = {key: value for key, value in gates.items() if key.startswith('z')}
# number = 0
# for index, (key, value) in enumerate(gates.items()):
#     number += (2 ** index) * value
# print(number)

# gold
# x = 0
# xgates = {key: value for key, value in original_gates.items() if key.startswith('x')}
# for index, (key, value) in enumerate(xgates.items()):
#     x += (2 ** index) * value
# y = 0
# ygates = {key: value for key, value in original_gates.items() if key.startswith('y')}
# for index, (key, value) in enumerate(ygates.items()):
#     y += (2 ** index) * value
# z = x + y
# print(x, y, z)

# fix up
# ['x09', 'AND', 'y09', 'kfp']
# ['y09', 'XOR', 'x09', 'hbs']
if ['x09', 'AND', 'y09', 'kfp'] in original_instructions:
    original_instructions.remove(['x09', 'AND', 'y09', 'kfp'])
    original_instructions.append(['x09', 'AND', 'y09', 'hbs'])
if ['y09', 'XOR', 'x09', 'hbs'] in original_instructions:
    original_instructions.remove(['y09', 'XOR', 'x09', 'hbs'])
    original_instructions.append(['y09', 'XOR', 'x09', 'kfp'])
# ['x18', 'AND', 'y18', 'z18'] 
# ['pvk', 'XOR', 'fwt', 'dhq']
if ['x18', 'AND', 'y18', 'z18']  in original_instructions:
    original_instructions.remove(['x18', 'AND', 'y18', 'z18'] )
    original_instructions.append(['x18', 'AND', 'y18', 'dhq'] )
if ['pvk', 'XOR', 'fwt', 'dhq'] in original_instructions:
    original_instructions.remove(['pvk', 'XOR', 'fwt', 'dhq'])
    original_instructions.append(['pvk', 'XOR', 'fwt', 'z18'])
# ['dcm', 'XOR', 'dbp', 'pdg']
# ['bqp', 'OR', 'gkg', 'z22']
if ['dcm', 'XOR', 'dbp', 'pdg']  in original_instructions:
    original_instructions.remove(['dcm', 'XOR', 'dbp', 'pdg'])
    original_instructions.append(['dcm', 'XOR', 'dbp', 'z22'])
if ['bqp', 'OR', 'gkg', 'z22'] in original_instructions:
    original_instructions.remove(['bqp', 'OR', 'gkg', 'z22'])
    original_instructions.append(['bqp', 'OR', 'gkg', 'pdg'])
# ['ckj', 'XOR', 'bch', 'jcp']
# ['ckj', 'AND', 'bch', 'z27']
if ['ckj', 'XOR', 'bch', 'jcp'] in original_instructions:
    original_instructions.remove(['ckj', 'XOR', 'bch', 'jcp'])
    original_instructions.append(['ckj', 'XOR', 'bch', 'z27'])
if ['ckj', 'AND', 'bch', 'z27'] in original_instructions:
    original_instructions.remove(['ckj', 'AND', 'bch', 'z27'] )
    original_instructions.append(['ckj', 'AND', 'bch', 'jcp'])


output_gates = {}
for index in range(0, 45):
    output_gate = 'z' + str(index).zfill(2)
    remaining_gates = [output_gate]
    while len(remaining_gates) > 0:
        current_gate = remaining_gates.pop()
        for element in original_instructions:
            if (element[3]) == current_gate:
                if output_gate not in output_gates:
                    output_gates[output_gate] = [[element[0], element[1], element[2], element[3]]]
                else:
                    output_gates[output_gate].append([element[0], element[1], element[2], element[3]])
                if not element[0].startswith('x') and not element[0].startswith('y') and element[0] not in remaining_gates:
                    remaining_gates.append(element[0])
                if not element[2].startswith('x') and not element[2].startswith('y') and element[2] not in remaining_gates:
                    remaining_gates.append(element[2])

diff_gates = {}
for index in range(0, 44):
    output_gate1 = 'z' + str(index).zfill(2)
    output_gate2 = 'z' + str(index + 1).zfill(2)
    diff1 = [x for x in output_gates[output_gate1] if x not in output_gates[output_gate2]]
    diff2 = [x for x in output_gates[output_gate2] if x not in output_gates[output_gate1]]
    diff = diff1 + diff2
    diff_gates[output_gate1 + " " + output_gate2] = diff
for key,value in diff_gates.items():
    print(key + ": ")
    print(value)
    print('\n')

import copy
gates = copy.deepcopy(original_gates)
for index, (key, value) in enumerate(output_gates.items()):
    if index > 10:
        break
    instructions = copy.deepcopy(value)
    while len(instructions) > 0:
        for instruction in instructions:
            input0 = instruction[0]
            input1 = instruction[2]
            operand = instruction[1]
            output = instruction[3]
            if input0 in gates and input1 in gates:
                if operand == 'AND':
                    gates[output] = gates[input0] & gates[input1]
                elif operand == 'OR':                
                    gates[output] = gates[input0] | gates[input1]
                elif operand == 'XOR':
                    if gates[input0] == gates[input1]:
                        gates[output] = 0
                    else:
                        gates[output] = 1
                instructions.remove(instruction)
                break
gates = dict(sorted(gates.items()))
gates = {key: value for key, value in gates.items() if key.startswith('z')}
number = 0
for index, (key, value) in enumerate(gates.items()):
    number += (2 ** index) * value
print(number)

# good_instructions = [ \
# ['x00', 'XOR', 'y00', 'z00'],
# ['qgt', 'XOR', 'gwq', 'z01'], ['y00', 'AND', 'x00', 'gwq'], ['y01', 'XOR', 'x01', 'qgt']
# ]