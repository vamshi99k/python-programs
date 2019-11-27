s='137'
res=''
for i in range(len(s)):
	if s[len(s)-1]!='7' and s[i]=='7':
		res=res+s[i+1: : ]
		"""
	elif s[len(s)-1]=='7':
		res=res+'-1'
	else:
		res=res+s[i]
print(res)