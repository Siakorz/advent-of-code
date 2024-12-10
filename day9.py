with open("inputs/inputDay9.txt", "r") as f:
    diskMap, layout, fileId = [], [], 0
    for line in f:
        for char in line:
            diskMap.append(char)

for i in range(len(diskMap)):
    if not i % 2:
        for j in range(int(diskMap[i])):
            layout.append(fileId)
        fileId += 1
    else:
        for j in range(int(diskMap[i])):
            layout.append(".")

def rearange(i ,j, length, toInsert):
    for z in range(j, j+length+1):
        layout[z] = toInsert
    while length >= 0:
        layout[i + length] = "."
        length -= 1


def searchForSpace(i, length):
    j, z = 0, 0
    while j < i:
        if layout[j] == ".":
            temp = 0
            z = j
            if length == 0:
                rearange(i, z, length, layout[i])
                return True
            while layout[j] == ".":
                temp += 1
                j += 1
                if temp >= length and layout[j] == "." and layout[z] == ".":
                    rearange(i, z, length, layout[i])
                    return True
                if temp >= length:
                    break
        j += 1

i = len(layout) - 1
while i >= 0:
    length = 0
    while not layout[i] == "." and layout[i] == layout[i-1]:
        length += 1
        if i < 0:
            break
        i -= 1
    if not layout[i] == ".":
        searchForSpace(i, length)
    
    i -= 1

checkSum = 0
for i in range(len(layout)):
    if not layout[i] == ".":
        checkSum += i * layout[i]

print(checkSum)