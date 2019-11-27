string=input()
mystring='abcdefghijklmnopqrstuvwxyz'
c=0
for i in mystring:
	if i in string:
		c+=1
if c==26:
	print('panagram')
else:
	print('not panagram')
