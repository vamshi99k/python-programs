s='a4b3c2'
output=''
for i in s:
	if i.isalpha():
		output=output+i
		privious=i
	else:
		output=output+privious*(int(i)-1)
print(output)
