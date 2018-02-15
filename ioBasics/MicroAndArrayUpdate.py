T = int(raw_input())
A = []

for i in range(0, T):
	N, K = map(int, raw_input().split())
	A = map(int, raw_input().split())
	A = sorted(A)

	seconds = K - A[0]
	if seconds < 0:
		seconds = 0

	print seconds
	A = []
