with open("inputs/inputDay4.txt", "r") as f:
    wordSearch = []
    for line in f:
        wordSearch.append(line.replace("\n", ""))
timesAppeared = 0
for i in range(len(wordSearch)):
    for ii in range(len(wordSearch[i])):
        if i < len(wordSearch) - 2:
            if ii < len(wordSearch[i]) - 2:
                if wordSearch[i][ii] == "M" or wordSearch[i][ii] == "S":
                    if wordSearch[i][ii+2] == "M" or wordSearch[i][ii+2] == "S":
                        if wordSearch[i+1][ii+1] == "A":
                            if wordSearch[i][ii] == "M" and wordSearch[i+2][ii+2] == "S":
                                if wordSearch[i][ii+2] == "M" and wordSearch[i+2][ii] == "S":
                                    timesAppeared += 1
                                if wordSearch[i][ii+2] == "S" and wordSearch[i+2][ii] == "M":
                                    timesAppeared += 1
                            if wordSearch[i][ii] == "S" and wordSearch[i+2][ii+2] == "M":
                                if wordSearch[i][ii+2] == "M" and wordSearch[i+2][ii] == "S":
                                    timesAppeared += 1
                                if wordSearch[i][ii+2] == "S" and wordSearch[i+2][ii] == "M":
                                    timesAppeared += 1


print(timesAppeared)