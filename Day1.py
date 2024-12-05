import re

# Set up
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

# Silver star
result = 0
for index, number in enumerate(list1):
    result = result + abs(list1[index] - list2[index])
print(result)

# Gold star
similar = 0
for number1 in list1:
    time = 0
    for number2 in list2:
        if number1 == number2:
            time += 1
    similar += number1 * time
print(similar)