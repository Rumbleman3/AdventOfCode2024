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
for secret in secretnumbers:
    current = secret
    for i in range(0, totalIteration):
        current = ((current * 64) ^ current) % 16777216
        current = (int(current / 32) ^ current) % 16777216
        current = ((current * 2048) ^ current) % 16777216
    print(current)
    totalSecret += current
print(totalSecret)
