import re

# Set up
file = open("day3.input", "r")
content = file.read()
file.close()

# Silver star
operations = re.findall(r'mul\(\d+,\d+\)', content)
product = 0
for operation in operations:
    numbers = re.findall(r'\d+', operation)
    numbers = [int(number) for number in numbers]
    product += numbers[0] * numbers[1]
print(product)

# Gold star
operations = re.findall(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', content)
product = 0
skip = False
for operation in operations:
    if operation == 'do()':
        skip = False
        continue
    elif operation == 'don\'t()':
        skip = True
        continue
    
    if skip:
        continue
    else:
        numbers = re.findall(r'\d+', operation)
        numbers = [int(number) for number in numbers]
        product += numbers[0] * numbers[1]
print(product)