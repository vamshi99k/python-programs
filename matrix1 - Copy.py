n=int(input())
mylist=[]
for i in range(n):
	l=input().split()
	l=list(map(int,l))
	mylist.append(l)
for i in range(len(mylist)):
	for j in range(len(mylist)):
		print(mylist[i][j],end='')
	print()

