import re

# set up
rules = {}
manual = []
with open('Day5.input', 'r') as file:
    for line in file:
        rule = re.findall(r'\d+\|\d+', line)
        if len(rule) != 0:
            rule = re.findall(r'\d+', rule[0])
            if rule[0] in rules:
                rules[rule[0]].append(rule[1])
            else:
                newRule = [rule[1]]
                rules[rule[0]] = newRule
        elif line != '\n':
            pages = re.findall(r'\d+', line)
            manual.append(pages)

# silver star
middlePageSum = 0
incorrectPages = []
for pages in manual:
    correct = True
    for index, number in enumerate(pages):
        rule = rules.get(number)
        if rule is not None:
            for nextIndex in range(index + 1, len(pages)):
                if pages[nextIndex] not in rule:
                    correct = False
                    break
        if not correct:
            incorrectPages.append(pages)
            break
    if correct:
        middlePageSum += int(pages[len(pages) // 2])
print(middlePageSum)

# gold star
middlePageSum = 0
for pages in incorrectPages:    
    correct = False
    while (correct is False):        
        swapped = False
        for index, number in enumerate(pages):
            rule = rules.get(number)
            if rule is not None:
                for nextIndex in range(index + 1, len(pages)):
                    if pages[nextIndex] not in rule:
                        pages[index], pages[nextIndex] = pages[nextIndex], pages[index]
                        swapped = True
                        break
            if swapped:
                break
        if not swapped:
            correct = True
    middlePageSum += int(pages[len(pages) // 2])
print(middlePageSum)

        
            
