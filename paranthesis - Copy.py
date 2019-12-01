def paranthsis(input):
	stack=[]
	pchar={'(':')','{':'}','[':']'}
	for i in input:
		if i in pchar:
			stack.append(i)
		elif len(stack)==0 or pchar[stack.pop()]!=i:
			return False
	return len(stack)==0

input='{}[]()'
print(paranthsis(input))