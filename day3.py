with open("inputs/inputDay3.txt", "r") as f:
    memory = ""
    for line in f:
        memory += line
    
def checkDigits(line):
    if line[0: 4].isdigit():
        return 0 
    elif line[0: 3].isdigit():
        return 3
    elif line[0: 2].isdigit():
        return 2
    elif line[0].isdigit():
        return 1
    

def checkAndMultiply(line): 
    firstNumberDigits = checkDigits(line[0:4])
    if firstNumberDigits == 0:
        return 0
    elif firstNumberDigits == 1:
        if line[1] == ",":
            secondNumberDigits = checkDigits(line[2: 6])
        else:
            return 0
        if line[1+firstNumberDigits+secondNumberDigits] == ")":
            return int(line[0]) * int(line[2:2+secondNumberDigits])
        return 0
    elif firstNumberDigits == 2:
        if line[2] == ",":
            secondNumberDigits = checkDigits(line[3: 7])
        else:
            return 0
        if line[1+firstNumberDigits+secondNumberDigits] == ")":
            return int(line[0:2]) * int(line[3:3+secondNumberDigits])
        return 0
    elif firstNumberDigits == 3:
        if line[3] == ",":
            secondNumberDigits = checkDigits(line[4: 8])
        else:
            return 0
        if line[1+firstNumberDigits+secondNumberDigits] == ")":
            return int(line[0:3]) * int(line[4:4+secondNumberDigits])
        return 0

result, do = 0, True
for i in range(len(memory)):
    if memory[i:i+7] == "don't()" and do:
        do = False
    if memory[i:i+4] == "do()" and not do:
        do = True
    if memory[i:i+4] == "mul(" and do:
            result += checkAndMultiply(memory[i+4: -1])

print(result)