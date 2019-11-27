def rev(num):
	rev=0
	while num:
		rev=rev*10+num%10
		num=num//10
	return rev
if __name__ == '__main__':
	
	num=int(input())
    while True:
    a=str(num)
    b=a[::-1]
    num=int(b)+int(a)

    if num==rev(num):
    print(num)
    break
		

		    

		

