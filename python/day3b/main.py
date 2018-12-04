
cloth = {}

def calcOverlaps(claims) :
    global cloth
    cloth = {}
    for claim in claims:
        claimElements = claim.split()
        claimId = claimElements[0]
        claimCoords = claimElements[2].split(":")[0].split(",")
        claimSizes = claimElements[3].split("x")

        rectWidth = int(claimSizes[0])
        rectHeight = int(claimSizes[1])
        startingX = int(claimCoords[0])
        startingY = int(claimCoords[1])

        for x in range(startingX, rectWidth + startingX):
            for y in range(startingY, rectHeight + startingY):
                clothCoord = str(x) + "x" + str(y)

                if clothCoord not in cloth:
                    cloth[clothCoord] = 1
                else:
                    cloth[clothCoord] += 1

    overlaps = 0
    for claimedClothCoord in cloth:
        if cloth[claimedClothCoord] > 1:
            overlaps += 1

    return overlaps


def findFirstNonOverlappingClaim(claims):
    calcOverlaps(claims)
    for claim in claims:
        claimElements = claim.split()
        claimId = claimElements[0]
        claimCoords = claimElements[2].split(":")[0].split(",")
        claimSizes = claimElements[3].split("x")

        rectWidth = int(claimSizes[0])
        rectHeight = int(claimSizes[1])
        startingX = int(claimCoords[0])
        startingY = int(claimCoords[1])

        foundOverlaps = False
        for x in range(startingX, rectWidth + startingX):
            for y in range(startingY, rectHeight + startingY):
                clothCoord = str(x) + "x" + str(y)
                if cloth[clothCoord] > 1:
                    foundOverlaps = True

        if not foundOverlaps:
            return claimId[1:]

    return ""
