import main

def assertEquals(testId, expected, actual):
    if expected == actual:
        print(str(testId) + " - pass")
    else:
        print(str(testId) + " - FAIL - expecting " + str(expected) + " but got " + str(actual))

boxIds = []
boxIds.append("abcde")
boxIds.append("fghij")
boxIds.append("klmno")
boxIds.append("pqrst")
boxIds.append("fguij")
boxIds.append("axcye")
boxIds.append("wvxyz")
assertEquals(1, "fgij", main.calcSimilarBoxIds(boxIds))

boxIds = []
f = open("c:\\git\\advent-of-code-2018\\python\\day2b\\puzzle.txt", "r")
for line in f:
    boxIds.append(line)

print ("answer " + str(main.calcSimilarBoxIds(boxIds)))
