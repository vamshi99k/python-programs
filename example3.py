l=list(map(int,input().split()))
p=1
for i in l:
	p=p*i
print(p)
res=[]
for i in l:
	res.append(p//i)
print(res)