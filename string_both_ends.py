def string_both_ends(input):
	if len(input)<2:
		return -1
	return input[:2]+input[-2:]
input='wt'
print(string_both_ends(input))