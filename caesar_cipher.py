alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Function to code the message into Caesar Cipher:
def coder(message,offset):
	cipher = ""
	for letter in message:
		if letter in alphabet:
			letter_index = alphabet.index(letter)
			cipher += alphabet[(letter_index - offset) % len(alphabet)]
		elif letter in alphabet_cap:
			letter_index = alphabet_cap.index(letter)
			cipher += alphabet_cap[(letter_index - offset) % len(alphabet_cap)]
		else: #all the characters that are not letter will be added straight to the cipher
			cipher += letter
	return cipher

# Funtion to decode the cipher into text message (when knowing the offset):
def decoder(cipher,offset):
	decoded_message = ""
	for letter in cipher:
		if letter in alphabet:
			letter_index = alphabet.index(letter)
			decoded_message += alphabet[(letter_index + offset) % len(alphabet)]
		elif letter in alphabet_cap:
			letter_index = alphabet_cap.index(letter)
			decoded_message += alphabet_cap[(letter_index + offset) % len(alphabet)]
		else:
			decoded_message += letter
	return decoded_message


	
		

