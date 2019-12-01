def isprime(n):
	for i in range(2,n//2+1):
		if n%2==0:
			return False
		return True
x=int(input())
y=int(input())
for i in range(x,y+1):
	if isprime(i):
		print(i)