f = open("c:\\git\\advent-of-code-2018\\python\\day1a\\puzzle.txt", "r")
frequency = 0
for change in f:
    frequency += int(change)

print("answer " + str(frequency))
