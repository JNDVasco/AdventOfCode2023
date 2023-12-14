import re


# filename = './Day2/test.txt'
filename = './Day2/data.txt'

colors = ['red', 'green', 'blue']


lines = []

with open(file=filename, mode='r') as file:
    while line := file.readline():
        lines.append(line.rstrip())

print(lines)

# [Game #, R, G, B]
gameCubeAmount = []

for game, line in enumerate(lines, start=1):
    cubes = re.findall(r'(\d+) (\w+)', line)
    print(line)
    print(game, ": ", cubes)

    colorMax = [0, 0, 0]

    for count, color in cubes:
        for idx, cmpColor in enumerate(colors):
            if color == cmpColor:
                colorMax[idx] = max(int(count), colorMax[idx])  

    print(colorMax)
    gameCubeAmount.append([game, *colorMax])
    print('---')


finalSum = 0;

for game, r, g, b in gameCubeAmount:
    if r <= 12 and g <= 13 and b <= 14:
        finalSum += game

print(finalSum)