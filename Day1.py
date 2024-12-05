import re

file = open("day1.input", "r")
content = file.read()
file.close()
numbers = re.findall(r'\d+', content)
numbers = [int(number) for number in numbers]
list1 = []
list2 = []
for index, number in enumerate(numbers):
    if index % 2 == 0:
        list1.append(number)
    else:
        list2.append(number)

list1 = sorted(list1)
list2 = sorted(list2)
result = 0
for index, number in enumerate(list1):
    result = result + abs(list1[index] - list2[index])
print(result)
