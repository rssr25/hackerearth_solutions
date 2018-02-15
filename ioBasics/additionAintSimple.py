alphabetDict1 = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}
alphabetDict = {y:x for x,y in alphabetDict1.iteritems()} 
number = int(raw_input())
finalString = []

for i in range(0, number):
	string = list(raw_input())
	length = len(string)
	reversed_string = string[::-1]

	for i in range(0, length):
		addedValue = alphabetDict[string[i]] + alphabetDict[reversed_string[i]]
		if addedValue > 26:
			addedValue = addedValue - 26
			finalString.append(alphabetDict1[addedValue])
		else:
			finalString.append(alphabetDict1[addedValue])

	print "".join(finalString)
	finalString = []



