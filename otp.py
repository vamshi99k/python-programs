s='4365188'
res=''
l=s[1::2]
print(l)
for i in l:
	res+=str(int(i)**2)
print(res[:4])