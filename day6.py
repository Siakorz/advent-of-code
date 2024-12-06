with open("inputs/inputDay6.txt", "r") as f:
    situationMap, indexes, loopingMap = [], [0, 0], []
    for line in f:
        situationMap.append(list(line.replace("\n", "")))
        loopingMap.append(list(line.replace("\n", "")))


def resetMap(obsLineIndex, obsCharIndex):
    for i in range(len(loopingMap)):
        for ii in range(len(loopingMap[i])):
            if loopingMap[i][ii] == "X":
                loopingMap[i][ii] = "."
    loopingMap[startPos[0]][startPos[1]] = "^"
    loopingMap[obsLineIndex][obsCharIndex] = "."

def tryLooping(obsLineIndex, obsCharIndex):
    if loopingMap[obsLineIndex][obsCharIndex] == "^":
        return False
    loopingMap[obsLineIndex][obsCharIndex] = "#"
    indexes[0], indexes[1] = startPos[0], startPos[1]
    for i in range(9000):
        if moveGuard(indexes[0], indexes[1], loopingMap):
            resetMap(obsLineIndex, obsCharIndex)
            return False
    resetMap(obsLineIndex, obsCharIndex)
    return True

def checkIfLeaves(lineIndex, charIndex, direction):
    if direction == "^" and lineIndex == 0:
            situationMap[lineIndex][charIndex] = "X"
            return True
    if direction == "V" and lineIndex == len(situationMap) - 1:
            situationMap[lineIndex][charIndex] = "X"
            return True
    if direction == ">" and charIndex == len(situationMap[lineIndex]) - 1:
            situationMap[lineIndex][charIndex] = "X"
            return True
    if direction == "<" and charIndex == 0:
            situationMap[lineIndex][charIndex] = "X"
            return True
    return False


def moveGuard(line, char, fmap):
    if fmap[line][char] == "^":
        if checkIfLeaves(line, char, "^"):
            return True
        if fmap[line-1][char] == "#":
            fmap[line][char] = ">"
        else:
            fmap[line-1][char] = "^"
            fmap[line][char] = "X"
            indexes[0] -= 1

    elif fmap[line][char] == "V":
        if checkIfLeaves(line, char, "V"):
            return True
        if fmap[line+1][char] == "#":
            fmap[line][char] = "<"
        else:
            fmap[line+1][char] = "V"
            fmap[line][char] = "X"
            indexes[0] += 1

    elif fmap[line][char] == ">":
        if checkIfLeaves(line, char, ">"):
            return True
        if fmap[line][char+1] == "#":
            fmap[line][char] = "V"
        else:
            fmap[line][char+1] = ">"
            fmap[line][char] = "X"
            indexes[1] += 1

    elif fmap[line][char] == "<":
        if checkIfLeaves(line, char, "<"):
            return True
        if fmap[line][char-1] == "#":
            fmap[line][char] = "^"
        else:
            fmap[line][char-1] = "<"
            fmap[line][char] = "X"
            indexes[1] -= 1
    return False

startPos = [0, 0]
for i in range(len(situationMap)):
    for ii in range(len(situationMap[i])):
        if situationMap[i][ii] == "^":
            startPos[0] = i
            startPos[1] = ii
            indexes[0] = i
            indexes[1] = ii
        
while not moveGuard(indexes[0], indexes[1], situationMap):
    pass

positions, looped = 0, 0

    
for i in range(len(situationMap)):
    for ii in range(len(situationMap[i])):
        if situationMap[i][ii] == "X":
            if tryLooping(i, ii):
                looped += 1
            positions += 1

print(positions)
print(looped)