cipherText = raw_input()
listText = list(cipherText)
capitals = range(65, 91)
smalls = range(97, 123)
nums = range(48, 58)

k = int(raw_input())

for i in range(0, len(listText)):
	asc = ord(listText[i])
	if asc in capitals:
		for j in range(0, k):
			asc = asc + 1
			if asc > 90:
				asc = 65
		listText[i] = chr(asc)
		asc = None


	elif asc in smalls:
		for l in range(0, k):
			asc = asc + 1
			if asc > 122:
				asc = 97
			else:
				continue
		listText[i] = chr(asc)
		asc = None

	elif asc in nums:
		for m in range(0, k):
			asc = asc + 1
			if asc > 57:
				asc = 48
			else:
				continue
		listText[i] = chr(asc)
		asc = None

	else:
		continue

print "".join(listText)


