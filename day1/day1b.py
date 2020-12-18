input = open("input.txt").readlines()

for i in range(len(input)):
    factor1 = int(input[i])
    for j in range(i, len(input)):
        factor2 = int(input[j])
        for k in range(j, len(input)):
            factor3 = int(input[k])
            if factor1 + factor2 + factor3 == 2020:
                print(factor1 * factor2 * factor3)
