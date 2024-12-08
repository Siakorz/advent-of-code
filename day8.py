with open("inputs/inputDay8.txt") as f:
    antennas = []
    for line in f:
        antennas.append(line.replace("\n", ""))

frequencies = []
for lineIndex in range(len(antennas)):
    for charIndex in range(len(antennas[lineIndex])):
        if not antennas[lineIndex][charIndex] == ".":
            frequencies.append([antennas[lineIndex][charIndex], lineIndex, charIndex])

frequencies.sort()

anitnodes, uniquePositions = 0, []

for n in range(len(frequencies) - 1, 0, -1):
    for i in range(n):
        if frequencies[n][0] == frequencies[i][0]:
            deltaY, deltaX = abs(frequencies[n][1] - frequencies[i][1]), abs(frequencies[n][2] - frequencies[i][2])
            for z in range(1, len(frequencies)):
                pos1 = [frequencies[n][1] + deltaY * z if frequencies[n][1] < frequencies[i][1] else frequencies[n][1] - deltaY * z, frequencies[n][2] + deltaX * z if frequencies[n][2] < frequencies[i][2] else frequencies[n][2] - deltaX * z]
                pos2 = [frequencies[i][1] - deltaY * z if frequencies[n][1] < frequencies[i][1] else frequencies[i][1] + deltaY * z, frequencies[i][2] - deltaX * z if frequencies[n][2] < frequencies[i][2] else frequencies[i][2] + deltaX * z]
                if 0 <= pos1[0] < len(antennas[0]) and 0 <= pos1[1] < len(antennas) and pos1 not in uniquePositions:
                    anitnodes += 1
                    uniquePositions.append(pos1)
                if 0 <= pos2[0] < len(antennas[0]) and 0 <= pos2[1] < len(antennas) and pos2 not in uniquePositions:
                    anitnodes += 1
                    uniquePositions.append(pos2)

print(anitnodes)