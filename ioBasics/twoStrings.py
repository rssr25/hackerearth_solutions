num_test = int(raw_input())

for i in range(0, num_test):
	word1, word2 = map(str, raw_input().split())

	word1 = "".join(sorted(word1))
	word2 = "".join(sorted(word2))

	if(word1 == word2):
		print 'YES'
	else:
		print 'NO'
