check_string='aaaabbbcc'
d = {}
for x in check_string:
  if d.keys():
    d[x]+= 1
  else:
    d[x]= 1

for key in d.items():
  if d[key] > 1:
    print(key, count[key])