s='aaabcccdfshsrhn'
d={}
for x in s:
	if x in d.keys():
		d[x]=d[x]+1
	else:
		d[x]=1
for k,v in d.items():
	print('{}  {}'.format(k,v))