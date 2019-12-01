n=int(input())
phonebook={}
for i in range(n):
	x=input().split()
	phonebook[x[0]]=x[1]
while True:
	try:
		x=input()
	except:
		break
	if x in phonebook:
		print(x+'='+phonebook[x])
	else:
		print('Not found')