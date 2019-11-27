n=int(input())
r=0
c=0
temp=n
while n>0:
	r=n%10
	c=c+(r*r*r)
	n=n//10
n=temp
if temp==c:
	print('armstrong')
else:
	print('not armstrong number')

