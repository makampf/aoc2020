input = open("input.txt").readlines()

sumValid = 0
for line in input:
    policy = line.split()
    borders = policy[0].split("-")
    pos1 = int(borders[0])
    pos2 = int(borders[1])
    letter = policy[1][:1]
    password = policy[2]

    if (
        password[pos1 - 1] == letter
        and password[pos2 - 1] != letter
        or password[pos1 - 1] != letter
        and password[pos2 - 1] == letter
    ):
        sumValid += 1

print(sumValid)