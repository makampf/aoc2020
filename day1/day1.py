input = open("input.txt").readlines()

for i in range(len(input)):
    for j in range(i, len(input)):
        if int(input[i]) + int(input[j]) == 2020:
            print(int(input[i]) * int(input[j]))
