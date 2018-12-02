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



boxIds = []
boxIds.append("")
print (calcChecksum(boxIds) == 0)

boxIds = []
boxIds.append("aa")
boxIds.append("bbb")
print (calcChecksum(boxIds) == 1)

boxIds = []
boxIds.append("aab")
boxIds.append("abbb")
print (calcChecksum(boxIds) == 1)

boxIds = []
boxIds.append("abcdef")
boxIds.append("bababc")
boxIds.append("abbcde")
boxIds.append("abcccd")
boxIds.append("aabcdd")
boxIds.append("abcdee")
boxIds.append("ababab")
print (calcChecksum(boxIds) == 12)

boxIds = []
f = open("python/day2a/puzzle.txt", "r")
for line in f:
    boxIds.append(line)

print ("answer " + str(calcChecksum(boxIds)))
