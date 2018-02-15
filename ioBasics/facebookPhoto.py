l = int(raw_input())
n = int(raw_input())

for i in range(0, n):
	w, h = map(int, raw_input().split())
	if w==l and h==l:
		print "ACCEPTED"
	elif (w==h and w>l) and (w==h and h>l)
		print "ACCEPTED"
	elif w > l and h == l:
		print "CROP IT"
	elif w ==l and h>l:
		print "CROP IT"
	elif w > l and h > l:
		print "CROP IT"
	else:
		print "UPLOAD ANOTHER"
