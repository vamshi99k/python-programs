def netamount(transction):
	temp_d=[]
	temp_w=[]
	for i in transction:
		if 'D' in i:
			temp_d.append(i)
		if 'W' in i:
			temp_w.append(i)
		dlist=[int(i.split(':')[1]) for i in temp_d]
		wlist=[int(i.split(':')[1]) for i in temp_w]
		netamt=sum(dlist)-sum(wlist)
	return netamt
transction=['D:300','D:200','W:200','D:100']
print(netamount(transction))