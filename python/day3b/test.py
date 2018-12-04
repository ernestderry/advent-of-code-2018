import main

def assertEquals(testId, expected, actual):
    if expected == actual:
        print(str(testId) + " - pass")
    else:
        print(str(testId) + " - FAIL - expecting " + str(expected) + " but got " + str(actual))


claims = []
assertEquals(1, 0, main.calcOverlaps(claims))

claims = []
claims.append("#1 @ 0,0: 1x1")
claims.append("#2 @ 0,0: 1x1")
assertEquals(2, 1, main.calcOverlaps(claims))

claims = []
claims.append("#1 @ 0,0: 5x1")
claims.append("#2 @ 0,0: 5x1")
assertEquals(3, 5, main.calcOverlaps(claims))

claims = []
claims.append("#1 @ 0,0: 1x5")
claims.append("#2 @ 0,0: 1x5")
assertEquals(4, 5, main.calcOverlaps(claims))

claims = []
claims.append("#1 @ 0,0: 5x5")
claims.append("#2 @ 0,0: 5x5")
assertEquals(5, 25, main.calcOverlaps(claims))

claims = []
claims.append("#1 @ 10,10: 5x5")
claims.append("#2 @ 10,10: 5x5")
assertEquals(6, 25, main.calcOverlaps(claims))

claims = []
claims.append("#1 @ 0,0: 5x1")
claims.append("#2 @ 1,0: 5x1")
assertEquals(7, 4, main.calcOverlaps(claims))

claims = []
claims.append("#1 @ 0,0: 1x5")
claims.append("#2 @ 0,1: 1x5")
assertEquals(8, 4, main.calcOverlaps(claims))

claims = []
claims.append("#1 @ 0,0: 2x2")
claims.append("#2 @ 1,1: 2x2")
assertEquals(9, 1, main.calcOverlaps(claims))

claims = []
claims.append("#1 @ 10,10: 5x5")
claims.append("#2 @ 12,12: 5x5")
assertEquals(10, 9, main.calcOverlaps(claims))

f = open("c:\\git\\advent-of-code-2018\\python\\day3b\\puzzle.txt", "r")
claims = []
for line in f:
    claims.append(line)

print("answer is " + str(main.findFirstNonOverlappingClaim(claims)))
