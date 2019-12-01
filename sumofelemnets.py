def sum_of_elements(list,num):
	res=0
	ln=len(list)
	for i in range(1,ln-1):
		if list[i-1]!=num and list[i+1]!=num and list[i]!=num:
			res+=list[i]
		if list[0]!=num and list[1]!=num:
			res+=list[0]
		if list[ln-2]!=num and list[ln-1]!=num:
			res+=list[ln-1]
	return res
list=[1,7,3,4,1,7,10,5]
num=7
print(sum_of_elements(list,num))
