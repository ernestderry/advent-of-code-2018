def calcSimilarBoxIds(boxIds):
    letterIndex = 0
    numberOfBoxIds = len(boxIds)
    similarBoxId = ""
    while similarBoxId == "" and letterIndex < numberOfBoxIds - 1:
        for boxIdx in range(numberOfBoxIds):
            boxId = boxIds[boxIdx]
            newBoxId = boxId[0:letterIndex] + boxId[letterIndex + 1 : 999]
            for boxIdx2 in range(boxIdx + 1, numberOfBoxIds):
                boxId2 = boxIds[boxIdx2]
                newBoxId2 = boxId2[0:letterIndex] + boxId2[letterIndex + 1 : 999]
                if newBoxId == newBoxId2:
                    similarBoxId = newBoxId
                    break
            if similarBoxId != "":
                break
        letterIndex += 1
    return similarBoxId

boxIds = []
boxIds.append("abcde")
boxIds.append("fghij")
boxIds.append("klmno")
boxIds.append("pqrst")
boxIds.append("fguij")
boxIds.append("axcye")
boxIds.append("wvxyz")
print (calcSimilarBoxIds(boxIds) == "fgij")

boxIds = []
f = open("python/day2a/puzzle.txt", "r")
for line in f:
    boxIds.append(line)

print ("answer " + str(calcSimilarBoxIds(boxIds)))
