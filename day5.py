import math
with open("inputs/temp.txt") as f:
    rules, updates = [], []
    for line in f:
        if "|" in line:
            rules.append(line.replace("\n", "").split("|"))
        elif "," in line:
            updates.append(line.replace("\n", "").split(","))

def tryToFix(mainValueId, comparedValue, isBigger, line):
    temp: list = line.copy()
    for x in range(len(line)):
        if line[x] == comparedValue:
            comparedValueId = x
    temp.pop(comparedValueId)
    temp.insert(mainValueId + 1 if isBigger else mainValueId, comparedValue)
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
                    return False
    return True

def returnMiddle(line):
    mid = math.floor(len(line)/2)
    return int(line[mid])

correctUptades, middleValue, incorrectUpdates = [], 0, []
for line in updates:
    if check(line):
        correctUptades.append(line)

        

for line in correctUptades:
    middleValue += returnMiddle(line)
print(middleValue)