def count_letters_digits(sentence):
	letter_count=0
	digit_count=0
	for letter in sentence:
		if letter.isdigit():
			digit_count+=1
		if letter.isalpha():
			letter_count+=1
		result=[letter_count,digit_count]
	return result
sentence='hi bro how are 9999'
print(count_letters_digits(sentence))
