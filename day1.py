from pathlib import Path
lists = Path("inputs/inputDay1.txt").read_text().replace("\n", "   ").split("   ")
leftList, rightList, distance, similarity = [], [], 0, 0

for i, x in enumerate(lists):
    leftList.append(int(x)) if i % 2 == 0 else rightList.append(int(x))

leftList.sort()
rightList.sort()
for i in range(len(leftList)):
    x, y = leftList[i], rightList[i]
    distance += abs(x - y)
    similarity += x * rightList.count(x)

print("--------------------")
print(f"Distance: {distance}")
print("--------------------")
print(f"Similarity: {similarity}")
print("--------------------")