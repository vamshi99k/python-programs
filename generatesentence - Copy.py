def generatesen(subjects,verbs,objects):
	res=''
	l=[]
	for i in range(len(subjects)):
		for j in range(len(verbs)):
			for k in range(len(objects)):
				res+="%s %s %s,\n" %(subjects[i],verbs[j],objects[k])
	print(res)
    
	return l
subjects=['i','you']
verbs=['love','play']
objects=['basketball','football']
print(generatesen(subjects,verbs,objects))