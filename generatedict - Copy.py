def dictionary(num):
	d={}
	d={i:i**2 for i in range(1,num+1)}
	return d
num=10
print(dictionary(num))