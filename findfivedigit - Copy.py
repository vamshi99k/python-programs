def find_five_digit(): #start writing your code here 
   num2 = 0
   num3 = 0 
   num4 = 0 
   num5 = 0 
   for i in range(9,-1,-1): 
   	  num2=int(i-2) 
   	  num3=int(num2-2) 
   	  num4=int(num3-2) 
   	  num5=int(num3) 
   	  if(num3+num4+num5==i and num2+num3+num4+num5+i==19): 
   	  	  break 
   s=str(i)+str(num2)+str(num3)+str(num4)+str(num5) 
   print(s)
find_five_digit()
