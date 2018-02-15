test_cases = int(raw_input())

for i in range(0, test_cases):

	string1 = raw_input()
	string2 = raw_input()
	finalCount = 0

	len1 = len(string1)
	len2 = len(string2)

	string1 = "".join(sorted(set(string1)))
	string2 = "".join(sorted(set(string2)))

	sorted_len1 = len(string1)
	sorted_len2 = len(string2)

	finalCount = abs(sorted_len1 - sorted_len2) + abs(len1 - len2)

	smaller = len1 if sorted_len1 < sorted_len2 else sorted_len2

	for i in range(0, smaller):
		if string1[i] in string2:
			finalCount += 0
		else:
			finalCount+=2

	print finalCount