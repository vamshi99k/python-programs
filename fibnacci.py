def fibnacci(n):
	a=0
	b=1
	print(a)
	print(b)
	for i in range(2,n):
		c=a+b
		a,b=b,c
		print(c)
if __name__ == '__main__':
   n=int(input())
   fibnacci(n)