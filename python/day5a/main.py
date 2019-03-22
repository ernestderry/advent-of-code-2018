def unitsReact(unit1, unit2):
    return unit1 != unit2 and unit1.lower() == unit2.lower()

def processReactions(polymer):

    polymerChanged = True
    while polymerChanged:
        polymerChanged = False
        polymerLength = len(polymer)
        unitPos = 0
        unitsReactPos = -1
        newPolymer = ""
        while unitPos <= polymerLength-1:
            unit1 = polymer[unitPos : unitPos + 1]
            unit2 = polymer[unitPos + 1 : unitPos + 2]

            if unitsReact(unit1, unit2):
                polymerChanged = True
                unitPos += 2
            else:
                newPolymer += unit1
                unitPos += 1

        polymer = newPolymer

    return polymer
