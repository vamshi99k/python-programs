def solution(prices):
	d={}
	for k,v in prices.items():
		if v>200:
			d[k]=v
	return d
prices={'ACME':45.22,'AAPL':612.78,'IBM':205.55,'HPQ':37.20,'FBI':10.75}
print(solution(prices))

