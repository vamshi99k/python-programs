n=int(input())
d={}
for i in range(n):
	x=input().split()
	d[x[0]]=x[1]
while True:
	try:
		x=input()
	except:
		break
	if x in d:
		print(x+'='+d[x])
	else:
		print('not found')
