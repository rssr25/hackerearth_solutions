string = raw_input()
reverseString = "".join(reversed(string))

if string == reverseString:
	print "YES"
else:
	print "NO"