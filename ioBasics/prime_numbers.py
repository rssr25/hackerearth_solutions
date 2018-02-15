num = int(raw_input())
prime = []

def isPrime(num):

	isPrime = False

	for i in range(num-1, 1, -1):
		if(num%i == 0):
			isPrime = False
			return isPrime
		else:
			isPrime = True

	return isPrime

for i in range(3,num+1):
	if(isPrime(i)):	
		prime.append(i)
	else:
		continue

for j in range(0, len(prime)):
	print prime[i], 


