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
best_prices = {}
for index, (key, value) in enumerate(differences.items()):
    local_best_prices = {}
    for index2 in range(0, len(value) - 4):
        difference = (value[index2], value[index2 + 1], value[index2 + 2], value[index2 + 3])
        price = sequences[key][index2 + 4]
        if difference not in local_best_prices:
            local_best_prices[difference] = [key, price, index2 + 4]
        # else:            
        #     if local_best_prices[difference][1] < price:                    
        #         local_best_prices[difference][1] = price                
        #         local_best_prices[difference][2] = index2 + 4
    for index2, (key2, value2) in enumerate(local_best_prices.items()):
        if key2 not in best_prices:
            best_prices[key2] = [value2]
        else:
            best_prices[key2].append(value2)

# find the biggest set
best_difference = ()
best_price = -1
best_value = []
for index, (key, value) in enumerate(best_prices.items()):
    total = 0
    for element in value:
        total += element[1]
    if total > best_price:
        best_price = total
        best_difference = key
        best_value = value
print(best_difference, best_price, best_value)
# check
for element in best_value:
    key = element[0]
    price = element[1]
    index = element[2]
    if sequences[key][index] != price or \
        sequences[key][index - 1] != price - best_difference[3] or \
        sequences[key][index - 2] != price - best_difference[3] - best_difference[2] or \
        sequences[key][index - 3] != price - best_difference[3] - best_difference[2] - best_difference[1] or \
        sequences[key][index - 4] != price - best_difference[3] - best_difference[2] - best_difference[1] - best_difference[0]:
        print("error - " + str(key) + " - " + str(price) + " - " + str(index))

