import math

primeList = []
finalAlphabets = []
for i in range(65, 91):
	if i>1:
		for j in range(2, int(math.sqrt(i)) + 1):
			if (i%j) == 0:
				break;
		else:
			primeList.append(i)



test_cases = int(raw_input())

for i in range(0, test_cases):
	length = int(raw_input())
	string = raw_input()

	for letter in string:
		difference = 25
		asciiVal = ord(i)

		for value in primeList:
			if(abs(asciiVal - value) < difference):
				if(abs(asciiVal - value) == difference)
				difference = abs(asciiVal - value)






