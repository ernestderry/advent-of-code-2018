frequency = 0
frequencies = set()
foundRepeatedFrequency = False
while not foundRepeatedFrequency:
    f = open("python/day1b/puzzle.txt", "r")
    for change in f:
        frequency += int(change)
        if (frequency in frequencies):
            print("answer " + str(frequency))
            foundRepeatedFrequency = True
            break
        frequencies.add(frequency)
