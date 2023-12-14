import re


# filename = './Day1/test.txt'
filename = './Day1/data.txt'

lines = []

with open(file=filename, mode='r') as file:
    while line := file.readline():
        lines.append(line.rstrip())

print(lines)

linesIntegers = []

for line in lines:
    numbers = re.findall(r'\d', line)
    linesIntegers.append(numbers)

print(linesIntegers)


integers = []


for line in linesIntegers:
    integers.append(int(str(line[0]) + str(line[-1])))

print(integers)
print(sum(integers))

