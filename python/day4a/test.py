import main

def assertEquals(testId, expected, actual):
    if expected == actual:
        print(str(testId) + " - pass")
    else:
        print(str(testId) + " - FAIL - expecting " + str(expected) + " but got " + str(actual))

events = []
events.append("[1518-11-01 00:00] Guard #10 begins shift")
events.append("[1518-11-01 00:05] falls asleep")
events.append("[1518-11-01 00:25] wakes up")
events.append("[1518-11-01 00:30] falls asleep")
events.append("[1518-11-01 00:55] wakes up")
events.append("[1518-11-05 00:45] falls asleep")
events.append("[1518-11-01 23:58] Guard #99 begins shift")
events.append("[1518-11-02 00:40] falls asleep")
events.append("[1518-11-02 00:50] wakes up")
events.append("[1518-11-03 00:05] Guard #10 begins shift")
events.append("[1518-11-03 00:24] falls asleep")
events.append("[1518-11-03 00:29] wakes up")
events.append("[1518-11-04 00:02] Guard #99 begins shift")
events.append("[1518-11-04 00:36] falls asleep")
events.append("[1518-11-04 00:46] wakes up")
events.append("[1518-11-05 00:03] Guard #99 begins shift")
events.append("[1518-11-05 00:55] wakes up")

assertEquals(1, 240, main.calcSleepingGuardValue(events))

f = open("c:\\users\\Ernest\\git\\advent-of-code-2018\\python\\day4a\\puzzle.txt", "r")
events = []
for line in f:
    events.append(line)
    
print("answer is " + str(main.calcSleepingGuardValue(events)))
