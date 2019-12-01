def solution(s):
	res=''
	for i in range(len(s)):
		t=''
		for j in range(i,len(s)):
			if s[j] in t:
				break
			else:
				t=t+s[j]
		if len(t)>len(res):
			
		  res=t
	return res
if __name__ == '__main__':
	s='abcdacbxy'
	print(solution(s))
