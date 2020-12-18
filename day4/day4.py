input = open("input.txt").read()

passports = input.split("\n\n")

sumValidPassports = 0
requiredFields = {"byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"}
optionalFields = {"cid:"}
for passport in passports:
    isValidPassport = True
    for field in requiredFields:
        if field not in passport:
            isValidPassport = False
            break
    if isValidPassport:
        sumValidPassports += 1

print(sumValidPassports)
