def is_leapyear(year):
	if ((year%400==0 or year%4==0) and (year%100!=0)):
		return True
	else:
		return False
year=int(input())

l=[]
while len(l)<15:
	if is_leapyear(year):
		l.append(year)
	year=year+1
print(l)

