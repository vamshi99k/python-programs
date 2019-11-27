s="38"

a=" "
if '7' in s:

	for i in range(len(s)):
		if s[i] =='7':
			a=s[i+1::]
			break
	if len(a)>0:
		p=1
		for i in a:
			p*=int(i)
		print(p)
	else:
		print('-1')
else:
	c=1
	for i in s:
		c*=int(i)
	print(c)


