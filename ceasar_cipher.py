logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
			'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
			'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
			'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
			'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
			's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def ceasar(start_text, shift_amount, cipher_direction):

	end_text = ""

	if cipher_direction == "decode":
		shift_amount *= -1



	for char in start_text:

		if char in alphabet:

			position = alphabet.index(char)

			new_postion = position + shift_amount

			new_letter = alphabet[new_postion]

			end_text +=  new_letter
		else:
			end_text += char

	print(f'The {process}d text is  : \t {end_text}')

print(logo)

should_end = False



while not should_end:

	
	process = input('Type \"encode\" to encrypt or Type \"decode\" to decrypt : \n').lower()


	text = input('Type your message : \n').lower()


	shift = int(input('Type the shift number : \n'))

	shift = shift % 26




	if process == "encode" or process == "decode":

			ceasar(text, shift, process)

			restart = input('Type \"Yes\" to restart. Otherwise \"No\" to end.: \n').lower()

			if restart == "no":
				should_end = True
				print('Good Bye')
	else:
		print('enter a valid command decode or encode')



