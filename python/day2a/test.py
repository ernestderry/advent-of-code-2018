import main

def assertEquals(testId, expected, actual):
    if expected == actual:
        print(str(testId) + " - pass")
    else:
        print(str(testId) + " - FAIL - expecting " + str(expected) + " but got " + str(b))

boxIds = []
boxIds.append("")
assertEquals(1, 0, main.calcChecksum(boxIds))

boxIds = []
boxIds.append("aa")
boxIds.append("bbb")
assertEquals(2, 1, main.calcChecksum(boxIds))

boxIds = []
boxIds.append("aab")
boxIds.append("abbb")
assertEquals(3, 1, main.calcChecksum(boxIds))

boxIds = []
boxIds.append("abcdef")
boxIds.append("bababc")
boxIds.append("abbcde")
boxIds.append("abcccd")
boxIds.append("aabcdd")
boxIds.append("abcdee")
boxIds.append("ababab")
assertEquals(4, 12, main.calcChecksum(boxIds))

boxIds = []
f = open("python/day2a/puzzle.txt", "r")
for line in f:
    boxIds.append(line)

print ("answer " + str(main.calcChecksum(boxIds)))
