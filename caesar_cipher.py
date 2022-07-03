alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Function to code the message into Caesar Cipher:
def coder(message, offset):
	cipher = ""
	for letter in message:
		if letter in alphabet:
			letter_index = alphabet.index(letter)
			cipher += alphabet[(letter_index - offset) % len(alphabet)]
		elif letter in alphabet_cap:
			letter_index = alphabet_cap.index(letter)
			cipher += alphabet_cap[(letter_index - offset) % len(alphabet_cap)]
		else:
			cipher += letter
	return cipher


