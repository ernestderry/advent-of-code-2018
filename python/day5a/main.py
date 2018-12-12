def unitsReact(unit1, unit2):
    return unit1 != unit2 and unit1.lower() == unit2.lower()

def processReactions(polymer):

    polymerChanged = True
    while polymerChanged:
        polymerLength = len(polymer)
        unitPos = 0
        unitsReactPos = -1
        while unitPos < polymerLength and unitsReactPos < 0:
            unit1 = polymer[unitPos : unitPos + 1]
            unit2 = polymer[unitPos + 1 : unitPos + 2]

            if unitsReact(unit1, unit2):
                unitsReactPos = unitPos

            unitPos += 1

        if unitsReactPos >= 0:
            polymer = polymer[0:unitsReactPos] + polymer[unitsReactPos+2:]
            polymerChanged = True
        else:
            polymerChanged = False

    return polymer
