def findupperlower(sentence):
	c1=0
	c2=0
	for i in sentence:
		if i.isupper():
			c1+=1
		if i.islower():
			c2+=1
	res=[c1,c2]
	return res
sentence='HeLLO worls99'
print(findupperlower(sentence))
