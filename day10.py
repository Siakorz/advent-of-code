import time

startTime = time.time()

with open("inputs/inputDay10.txt", "r") as f:
    hiking, paths, reached9 = [], [], []
    for line in f:
        hiking.append([char for char in line.replace("\n", "")])

def nextStep(start, height):
    up, down, left, right = False, False, False, False
    if start[0]+1 < len(hiking):
        if hiking[start[0]+1][start[1]] == str(height + 1):
            down = True
    if start[0]-1 >= 0:
        if hiking[start[0]-1][start[1]] == str(height + 1):
            up = True
    if start[1]+1 < len(hiking[start[0]]):
        if hiking[start[0]][start[1]+1] == str(height + 1):
            right = True 
    if start[1]-1 >= 0:
        if hiking[start[0]][start[1]-1] == str(height + 1):
            left = True
    return [down, up, right, left, start]

def lookForTrailHead(startPos, trail, height):
    if height == 9:
        if [startPos, trail[4]] not in reached9:
            reached9.append([startPos, trail[4]])
        paths.append(trail[4])
    
    if trail[0]:
        lookForTrailHead(startPos, nextStep([trail[4][0]+1, trail[4][1]], height + 1), height + 1)
    if trail[1]:
        lookForTrailHead(startPos, nextStep([trail[4][0]-1, trail[4][1]], height + 1), height + 1)
    if trail[2]:
        lookForTrailHead(startPos, nextStep([trail[4][0], trail[4][1]+1], height + 1), height + 1)
    if trail[3]:
        lookForTrailHead(startPos, nextStep([trail[4][0], trail[4][1]-1], height + 1), height + 1)

            
for lineIndex in range(len(hiking)):
    for charIndex in range(len(hiking[lineIndex])):
        if hiking[lineIndex][charIndex] == "0":
            temp = nextStep([lineIndex, charIndex], 0)
            lookForTrailHead([lineIndex, charIndex], temp, 0)

print(len(paths))
print(len(reached9))
print(f"======={time.time() - startTime}=======")