def factsum(n):
	sum=0
	for i in range(1,n+1):
		if n%i==0:
			sum+=i
	return sum
l=list(map(int,input().split()))
for i in l:
	sum=factsum(i)
	if sum in l:
		print(sum)

