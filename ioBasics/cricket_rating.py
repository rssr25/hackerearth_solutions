#this is nothing but a maximum subarray problem
#we will use kadane's algorithm to do this

number = int(raw_input())
if number <= 0:
	rating = None
else:
	rating = map(int, raw_input().split())

def find_max_subarray(array):
	if array is None:
		return None
	elif all(i >= 0 for i in rating):
		return sum(rating)
	elif all(i < 0 for i in rating):
		return max(rating)
	else:
		max_c = max_g = array[0]

		for i in range(1, len(rating)):
			max_c = max(array[i], max_c + array[i])
			if max_c > max_g:
				max_g = max_c

		return max_g


print find_max_subarray(rating)


