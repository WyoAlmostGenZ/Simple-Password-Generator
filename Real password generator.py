import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
		   'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
		   'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
def password_generator_beta():

	letter_pwd = ""
	for letter in range(random.randint(2, 6)):
		random_letters = random.choice(letters)
		letter_pwd += random_letters


	symbol_pwd = ""
	for symbol in range(random.randint(2, 6)):
		random_symbols = random.choice(symbols)
		symbol_pwd += random_symbols


	number_pwd = ""
	for number in range(random.randint(2, 6)):
		random_numbers = random.choice(numbers)
		number_pwd += random_numbers


	concatanted_pwd = letter_pwd + symbol_pwd + number_pwd

	list_concat_pwd = list(concatanted_pwd)
	random.shuffle(list_concat_pwd)

	password = ""
	for letter in list_concat_pwd:
		password += letter
	return password


print(password_generator_beta())