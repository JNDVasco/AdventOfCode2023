import re


filename = './Day1/test-part2.txt'
# filename = './Day1/data.txt'


digitConversion = [["one", "one1one"], 
                   ["two", "two2two"], 
                   ["three", "three3three"],
                   ["four", "four4four"],
                   ["five", "five5five"],
                   ["six", "six6six"],
                   ["seven", "seven7seven"],
                   ["eight", "eight8eight"],
                   ["nine", "nine9nine"]]


lines = []

with open(file=filename, mode='r') as file:
    while line := file.readline():
        lines.append(line.rstrip())

print(lines)


linesReplaced = []

for line in lines:

    for digit in digitConversion:
        line = line.replace(digit[0], str(digit[1]))
    linesReplaced.append(line)

print(linesReplaced)

linesIntegers = []

for line in linesReplaced:
    numbers = re.findall(r'\d', line)
    linesIntegers.append(numbers)

print(linesIntegers)


integers = []


for line in linesIntegers:
    integers.append(int(str(line[0]) + str(line[-1])))

print(integers)
print(sum(integers))

