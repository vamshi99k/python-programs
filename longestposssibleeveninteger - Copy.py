s='649463'
l=[]
for i in s:
	if i.isdigit():
		l.append(int(i))
l.sort(reverse=True)
if 0 in l:
	l.remove(0)
	l.append(0)
if 2 in l:
	l.remove(2)
	l.append(2)
if 4 in l:
	l.remove(4)
	l.append(4)
if 6 in l:
	l.remove(6)
	l.append(6)
if 8 in l:
	l.remove(8)
	l.append(8)
l=list(map(str,l))
a=''.join(l)
print(a)
	
	
	




