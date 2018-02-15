N, Q = map(int, raw_input().split())
theArray = []
theArray = map(str, raw_input().split())

for i in range(0, Q):
	queryList = []
	queryList = map(int, raw_input().split())
	if len(queryList) == 2:
		flipbit = queryList[1]
		if theArray[flipbit-1] == '0':
			theArray[flipbit-1] = '1'
		else:
			theArray[flipbit-1] = '0'

	else:
		L = queryList[1]
		R = queryList[2]
		subArray = []

		for i in range(L, R+1):
			subArray.append(theArray[i-1])

		subArray = "".join(subArray)
		binToInt = int(subArray, 2)

		if binToInt%2 == 0:
			print "EVEN"
		else:
			print "ODD"
