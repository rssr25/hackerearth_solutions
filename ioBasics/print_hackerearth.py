length = int(raw_input())
string = raw_input()
count_h = count_a = count_c = count_k = count_e = count_r = count_t = final_count = 0



if length < 11:
	print 0
else:
	for letter in string:
		if letter == 'h':
			count_h += 1
		elif letter == 'a':
			count_a += 1
		elif letter == 'c':
			count_c += 1
		elif letter == 'k':
			count_k += 1
		elif letter == 'e':
			count_e += 1
		elif letter == 'r':
			count_r += 1
		elif letter == 't':
			count_t += 1

	if(count_h == count_a and count_a == count_e and count_e == count_r):
		if(count_c == count_k and count_k == count_t):
			if(count_h >= 2 and count_c >= 1):
				if(count_h > count_c):
					if(count_h % 2 == 0 and count_c % 2 == 0):
						if(count_c * 2 <= count_h):
							final_count = count_c
						else:
							final_count = count_h/2;
					elif(count_h % 2 !=0 and count_c %2 !=0):
						if(count_c * 2 < count_h):
							final_count = count_c
						else:
							final_count = (h-1)/2
					elif(count_h % 2 == 0 and count_c%2 != 0):
						if(count_c * 2 <= count_h):
							final_count = count_c
						else:
							final_count = count_h/2;
					else:
						if(count_c * 2 < count_h):
							final_count = count_c
						else:
							final_count = (h-1)/2

					print final_count;
		else:
			print 0
	else:
		print 0