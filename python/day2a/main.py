def containsNumberOfEqualLetters(id, numberOfEqualLetters):
    letterDict = {}
    for letter in id:
        if letter in letterDict:
            letterDict[letter] += 1
        else:
            letterDict[letter] = 1
    #    print letterDict

    for letterCount in letterDict:
        if letterDict[letterCount] == numberOfEqualLetters:
            return True

    return False

def calcChecksum(boxIds):
    twoLetterCount = 0
    threeLetterCount = 0
    for id in boxIds:
        if containsNumberOfEqualLetters(id, 2):
            twoLetterCount += 1
        if containsNumberOfEqualLetters(id, 3):
            threeLetterCount += 1
    #print (str(twoLetterCount) + " " + str(threeLetterCount))
    return twoLetterCount * threeLetterCount
