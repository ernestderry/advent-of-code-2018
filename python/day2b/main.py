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
