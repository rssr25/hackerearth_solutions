n = int(raw_input())
marks = []

for i in range(0, n):
	point = int(raw_input())
	if(point == 0):
		if not marks:
			continue
		else:
			marks.pop()
	else:
		marks.append(point)

print sum(marks)

