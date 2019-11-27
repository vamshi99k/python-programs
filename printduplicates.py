s='aaabcsdsegsjsen'
l=[]
for i in s:
	if i not in l:
		l.append(i)

output=''.join(l)
print(output)