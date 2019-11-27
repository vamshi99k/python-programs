*l,k=input().split()
k=int(k)
l=list(map(int,l))
for i in range(0,len(l)-1):
	for j in range(i+1,len(l)):
		if l[i]+l[j]==k:
			print(l[i],l[j])
