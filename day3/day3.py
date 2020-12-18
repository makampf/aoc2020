input = open("input.txt").readlines()

sumTrees = 0

x = 0
shift = 3
modulo = len(input[0]) - 1

for i in range(1, len(input)):
    x = (x + shift) % modulo
    pos = input[i][x]
    if pos == "#":
        sumTrees += 1

print(sumTrees)
