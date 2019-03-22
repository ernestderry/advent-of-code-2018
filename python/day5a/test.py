import main

def assertEquals(testId, expected, actual):
    if expected == actual:
        print(str(testId) + " - pass")
    else:
        print(str(testId) + " - FAIL - expecting " + str(expected) + " but got " + str(actual))

assertEquals(1, "", main.processReactions(""))

assertEquals(2, "a", main.processReactions("a"))

assertEquals(3, "", main.processReactions("aA"))

assertEquals(4, "aB", main.processReactions("aB"))

assertEquals(5, "AA", main.processReactions("AA"))

assertEquals(6, "aa", main.processReactions("aa"))

assertEquals(7, "", main.processReactions("Aa"))

assertEquals(8, "Ba", main.processReactions("Ba"))

assertEquals(9, "B", main.processReactions("AaB"))

assertEquals(10, "B", main.processReactions("BAa"))

assertEquals(11, "BBBBBBZZZZZZ", main.processReactions("BBBBBBAaZZZZZZ"))

assertEquals(12, "", main.processReactions("aAaA"))

assertEquals(14, "E", main.processReactions("aAEBcCb"))

assertEquals(15, "dabCBAcaDA", main.processReactions("dabAcCaCBAcCcaDA"))


f = open("c:\\git\\advent-of-code-2018\\python\\day5a\\puzzle.txt", "r")
for line in f:
    print ("answer is " + str(len(main.processReactions(line))))
