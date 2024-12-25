# set up
import re
secretnumbers = []
with open('Day22.input', 'r') as file:
    for line in file:
        line = line.strip('\n')
        secretnumbers.append(int(line))

# silver
totalIteration = 2000
totalSecret = 0
sequences = {}
differences = {}
for secret in secretnumbers:
    current = secret    
    sequence = [secret % 10]
    difference = []
    for i in range(0, totalIteration):
        previous = current
        current = ((current * 64) ^ current) % 16777216
        current = (int(current / 32) ^ current) % 16777216
        current = ((current * 2048) ^ current) % 16777216
        sequence.append(current % 10)
        difference.append(current % 10 - previous % 10)
    sequences[secret] = sequence
    differences[secret] = difference
    totalSecret += current
print(totalSecret)

# gold
pricechanges = []
for difference in differences:
    for index in range(0, len(difference) - 4):
        price = [difference[index]
