def checkRecord(record):
    record = [int(x) for x in record]
    if record[0] > record[1]:
        record = record[::-1]

    for i in range(len(record) - 1):
        if record[i] >= record[i + 1]:
            return False
        if not (record[i + 1] - 4 < record[i] < record[i + 1] + 4):
            return False
    return True


with open("inputs/inputDay2.txt", "r") as f:
    records = []
    for line in f:
        line = line.replace("\n", "").split(" ")
        records.append(line)
    safeReports = 0
    for x in records:
        if checkRecord(x):
            safeReports += 1
        else:
            for i in range(len(x)):
                temp = x[0:i] + x[i+1:]
                if checkRecord(temp):
                    safeReports += 1
                    break;
    print(safeReports)