import math

n, qTests = map(int, raw_input().split())

nArray = list(map(int, raw_input().split()))
smallArray = []

for i in range(0, qTests):

	s, e = map(int, raw_input().split())

	for j in range(s-1, e):
		smallArray[j] = nArray[j]

	print int(math.ceil(sum(smallArray)/len(smallArray)))
