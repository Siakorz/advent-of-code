import math
with open("inputs/inputDay5.txt") as f:
    rules, updates = [], []
    for line in f:
        if "|" in line:
            rules.append(line.replace("\n", "").split("|"))
        elif "," in line:
            updates.append(line.replace("\n", "").split(","))

def tryToFix(mainValueId, comparedValue, isBigger, line):
    temp = []
    for x in range(len(line)):
        temp.append(line[x])
        if line[x] == comparedValue:
            comparedValueId = x
    temp.pop(comparedValueId)
    temp.insert(mainValueId, comparedValue)
    return temp
    
    

def checkPositions(mainValueId, comparedValue, isBigger, line):
    for i in range(len(line)):
        if not i == mainValueId:
            if line[i] == comparedValue:
                if isBigger and i < mainValueId:
                    return False
                if not isBigger and i > mainValueId:
                    return False
    return True

def check(line):
    for i in range(len(line)):
        for r in range(len(rules)):
            if line[i] == rules[r][0]:
                if not checkPositions(i, rules[r][1], True, line):
                    return [i, rules[r][1], True]
    return False

def returnMiddle(line):
    mid = math.floor(len(line)/2)
    return int(line[mid])

correctUptades, middleValue, correctedValue, corrected = [], 0, 0, []
for line in updates:
    if not check(line):
        correctUptades.append(line)
    else:
        a = check(line)
        temp = tryToFix(a[0], a[1], a[2], line)
        for i in range(10000):
            a = check(temp)
            if not a:
                corrected.append(temp)
                break;
            temp = tryToFix(a[0], a[1], a[2], temp)

for line in correctUptades:
    middleValue += returnMiddle(line)
for line in corrected:
    correctedValue += returnMiddle(line)
    
print(middleValue)
print(correctedValue)