input = open("input.txt").readlines()

sumValid = 0
for line in input:
    policy = line.split()
    borders = policy[0].split("-")
    mina = int(borders[0])
    maxa = int(borders[1])
    letter = policy[1][:1]
    password = policy[2]
    amount = password.count(letter)
    if mina <= amount <= maxa:
        sumValid += 1

print(sumValid)