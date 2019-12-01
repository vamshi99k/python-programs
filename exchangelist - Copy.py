def exchangelist(list):
	fh=[]
	sh=[]
	mid=len(list)//2
	ln=len(list)
	for i in list:
		if i in range(0,mid):
			fh.append(list[i])
		if i in range(mid,ln):
			sh.append(list[i])
	shr=sh[::-1]
	res=shr+fh
	return res
list=[1,2,3,4,5,6,7]
print(exchangelist(list))