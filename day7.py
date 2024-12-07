import itertools

with open("inputs/inputDay7.txt", "r") as f:
    equations = []
    for line in f:
        equations.append(list(map(int, line.replace("\n", "").replace(":", "").split())))

def checkEquation(line, operators):
    value, testValue = line[0], line[1]
    for i in range(len(operators)):
        if operators[i] == "+":
            testValue += line[i+2]
        if operators[i] == "*":
            testValue *= line[i+2]
        if operators[i] == "||":
            testValue = str(testValue) + str(line[i+2])
            testValue = int(testValue)
        if testValue > value:
            return False
    return True if value == testValue else False

def checkLine(line):
    possibleOperators = list(itertools.product(["+", "*", "||"], repeat=len(line) - 2))
    for operators in possibleOperators:
        if checkEquation(line, operators):
            return line[0]
        
total = 0
for x in equations:
    a = checkLine(x)
    if a:
        total += a

print(total)
        