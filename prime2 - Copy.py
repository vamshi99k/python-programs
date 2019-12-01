def isprime(n):
	for i in range(2,n//2+1):
		if n%2==0:
			return False
		return True
x=int(input())
count=0
i=2
while count<x:
	if isprime(i):
		print(i,)
		count+=1
	i+=1
