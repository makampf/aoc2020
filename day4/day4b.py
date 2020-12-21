input = open("input.txt").read()

passports = input.split("\n\n")

sumValidPassports = 0
requiredFields = {"byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"}
optionalFields = {"cid:"}
for passport in passports:
    isValidPassport = True
    for requiredField in requiredFields:
        if requiredField not in passport:
            isValidPassport = False
            break
    if isValidPassport:
        passport = passport.replace("\n", " ")
        fields = passport.split()
        for field in fields:
            kvpair = field.split(":")
            if condition:
                pass
            elif expression:
                pass
        isValidPassport = False
        if isValidPassport:
            sumValidPassports += 1


print(sumValidPassports)
