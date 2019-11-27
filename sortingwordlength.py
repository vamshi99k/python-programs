def sorted(l):
	for i in range(0,len(l)-1):
		for j in range(i+1,len(l)):
			if len(l[i])>len(l[j]):
				l[i],l[j]=l[j],l[i]
			elif l[i]==l[j] and l[i]>l[j]:
				l[i],l[j]=l[j],l[i]
	a=''.join(l)
	return l

	if __name__ == '__main__':
		l=input().split()
		print(sorted(l))