def check_22(num_list): #start writing your code here 
  desired = [2,2]
  if str(desired)[1:-1] in str(num_list): 
  	 return True 
  else: 
  	 return False
print(check_22([3,2,5,1,2,1,2,2]))
