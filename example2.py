l=list(map(int,input().split()))
l.sort()
res=[]
for i in range(0,len(l)//2):
	res.append(l[i])
	res.append(l[len(l)-1-i])
if len(l)%2==1:
	res.append(l[len(l)//2])
print(res)
#


input: '5 4 1 6 2 7 0 6'
output: 0 7 1 6 2 6 4 5
