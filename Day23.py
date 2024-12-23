# set up
import re
connections = {}
with open('Day23.input', 'r') as file:
    for line in file:
        line = line.strip('\n')
        connection = re.match(r'(\w+)-(\w+)', line)
        c1 = connection.group(1)
        c2 = connection.group(2)
        if c1 in connections and c2 not in connections[c1]:
            connections[c1].append(c2)
        else:
            connections[c1] = [c2]
        if c2 in connections and c1 not in connections[c2]:
            connections[c2].append(c1)
        else:
            connections[c2] = [c1]

# silver
triplets = []
for index1, (key1, value1) in enumerate(connections.items()):
    for index2, (key2, value2) in enumerate(connections.items()):
        if (index2 <= index1):
            continue
        if key1 in connections[key2] and key2 in connections[key1]:
            common = list(set(value1) & set(value2))
            for key3 in common:
                if key1 in connections[key3] and key2 in connections[key3]:
                    triplet = [key1, key2, key3]
                    triplet.sort()
                    if triplet not in triplets:
                        triplets.append(triplet)

tconnection = 0
for element in triplets:
    if element[0].startswith('t') or element[1].startswith('t') or element[2].startswith('t'):
        tconnection += 1
print(tconnection)

# gold star
import copy
set_collections = []
for key1, value1 in connections.items():
    connected_sets = []
    for element in value1:
        connected = [key1]
        for element2 in value1:
            if element2 == element or element2 in connections[element]:
                connected.append(element2)
        connected.sort()
        connected_sets.append(connected)
    set_collections.append(connected_sets)

confirmed_sets = []
from collections import Counter
for sets in set_collections:
    counted = {}
    for set in sets:
        tupleset = tuple(set)
        if tupleset in counted:
            counted[tupleset] += 1
        else:
            counted[tupleset] = 1
    for key, value in counted.items():
        if len(key) - 1 == value and key not in confirmed_sets:
            confirmed_sets.append(key)
confirmed_sets = sorted(confirmed_sets, key = lambda s: len(s))
print(confirmed_sets)

            
