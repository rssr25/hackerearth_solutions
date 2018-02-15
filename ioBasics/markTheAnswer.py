numOfQues, maxDifficulty = map(int, raw_input().split())
difficulty = []
difficulty = map(int, raw_input().split())
oneTimeSkip = False
counter = 0

for i in range(0, numOfQues):
	if difficulty[i] <= maxDifficulty:
		counter += 1
	elif difficulty[i] > maxDifficulty:
		if oneTimeSkip == False:
			oneTimeSkip = True
			continue
		else:
			break

print counter