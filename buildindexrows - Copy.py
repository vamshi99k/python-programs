def build_index_grid(rows, columns): 
	s='' 
	r=[] 
	for i in range(0,rows): 
		for j in range(0,columns): 
			if i==0 and j==0: 
				s+="[" 
			if j==0: 
				s+="[" 
			s+="'"+str(i)+","+str(j)+"'" 
			if (j!=(columns-1)): 
				s+="," 
			if j==(columns-1) and i!=(rows-1): 
				s+="]" 
			if j==(columns-1) and i==(rows-1): 
				s+="]]"
    
    
    return  
rows=4 
columns=3 
result=build_index_grid(rows,columns) 
print("Rows:",rows,"Columns:",columns) 
print("The matrix is:",result) 
for i in result: 
	print(i)
