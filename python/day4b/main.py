def calcSleepingGuardValue(events):
    guardTotalSleepTime = {}
    guardSleepMinuteTotals = {}
    events.sort()
    for event in events:
        eventBits = event.split()
        date = eventBits[0][1:11]
        time = eventBits[1][0:5]
        action = eventBits[2]
        guard = eventBits[3]
        if action == "Guard":
            shiftGuard = int(guard[1:])
            if shiftGuard not in guardTotalSleepTime:
                guardTotalSleepTime[shiftGuard] = 0
                guardSleepMinuteTotals[shiftGuard] = {}

        elif action == "falls":
            if time[0:2] != "00":
                sleepStart = 0
            else:
                sleepStart = int(time[3:5])

        elif action == "wakes":
            if time[0:2] != "00":
                sleepEnd = 60
            else:
                sleepEnd = int(time[3:5])
            for minute in range(sleepStart, sleepEnd):
                guardTotalSleepTime[shiftGuard] += 1
                if minute not in guardSleepMinuteTotals[shiftGuard]:
                    guardSleepMinuteTotals[shiftGuard][minute] = 1
                else:
                    guardSleepMinuteTotals[shiftGuard][minute] += 1

    highestSleepMinuteCount = 0
    highestSleepMinute = 0
    highestSleepMinuteGuard = 0
    for guard in guardSleepMinuteTotals:
        for minute in guardSleepMinuteTotals[guard]:
            if guardSleepMinuteTotals[guard][minute] > highestSleepMinuteCount:
                highestSleepMinuteCount = guardSleepMinuteTotals[guard][minute]
                highestSleepMinute = minute
                highestSleepMinuteGuard = guard

    print("highest sleep minute guard " + str(highestSleepMinuteGuard))
    print("highest sleep minute " + str(highestSleepMinute))

    return highestSleepMinuteGuard * highestSleepMinute
