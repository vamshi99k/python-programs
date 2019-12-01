def findnine(list):
	count=9
	res=[]
	for i in list[:4]:
		res.append(i)
	if count in res:
		return True
	else:
		return False
list=[1,2,3,9]
print(findnine(list))
