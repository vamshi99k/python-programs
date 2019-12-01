s='195'
while not s==s[::-1]:
	s=str(int(s)+int(s[::-1]))
print(s)