def findgcd(num1,num2):
	if num2==0:
		return num1
	else:
		return findgcd(num2,num2%num1)
num1=45
num2=9

print(findgcd(num1,num2))