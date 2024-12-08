import copy

# Setup
map = []
with open('Day8.input', 'r') as file:
    for line in file:
        line = line.replace('\n','')
        map.append(line)

# Silver and gold star
antennaGroups = {}
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] != '.':            
                if map[i][j] in antennaGroups:
                    antennaGroups[map[i][j]].append([i,j])
                else:
                    antenna = [[i,j]]
                    antennaGroups[map[i][j]] = antenna
antinodes = []
for antennas in antennaGroups.values():
    for antenna1 in antennas:
        for antenna2 in antennas:
            if antenna1 == antenna2:
                continue
            i = abs(antenna1[0] - antenna2[0])
            j = abs(antenna1[1] - antenna2[1])
            antinode1i = antenna1[0]
            antinode1j = antenna1[1]
            antinode = [antinode1i, antinode1j]
            if antinode not in antinodes:
                antinodes.append(antinode)
            condition = True
            while condition:
                if antenna1[0] < antenna2[0]:
                    antinode1i = antinode1i - i
                else:
                    antinode1i = antinode1i + i
                if antenna1[1] < antenna2[1]:
                    antinode1j = antinode1j - j
                else:
                    antinode1j = antinode1j + j
                if antinode1i >= 0 and antinode1i < len(map) and antinode1j >= 0 and antinode1j < len(map[i]):
                    antinode = [antinode1i, antinode1j]
                    if antinode not in antinodes:
                        antinodes.append(antinode)
                else:
                    condition = False
                    
            antinode2i = antenna2[0]
            antinode2j = antenna2[1]
            antinode = [antinode2i, antinode2j]
            if antinode not in antinodes:
                antinodes.append(antinode)
            condition = True
            while condition:
                if antenna2[0] < antenna1[0]:
                    antinode2i = antinode2i - i
                else:
                    antinode2i = antinode2i + i
                if antenna2[1] < antenna1[1]:
                    antinode2j = antinode2j - j
                else:
                    antinode2j = antinode2j + j
                if antinode2i >= 0 and antinode2i < len(map) and antinode2j >= 0 and antinode2j < len(map[i]):
                    antinode = [antinode2i, antinode2j]
                    if antinode not in antinodes:
                        antinodes.append(antinode)
                else:
                    condition = False
                    
print(len(antinodes))
     