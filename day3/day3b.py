input = open("input.txt").readlines()

modulo = len(input[0]) - 1
prodTrees = 1

for shift in [1, 3, 5, 7]:
    x = 0
    sumTrees = 0
    for i in range(1, len(input)):
        x = (x + shift) % modulo
        pos = input[i][x]
        if pos == "#":
            sumTrees += 1
    prodTrees *= sumTrees

x = 0
shift = 1
sumTrees = 0
for i in range(2, len(input), 2):
    x = (x + shift) % modulo
    pos = input[i][x]
    if pos == "#":
        sumTrees += 1
prodTrees *= sumTrees

print(prodTrees)
