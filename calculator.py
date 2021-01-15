logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
import os

def add(n1, n2):
	return n1 + n2
def sub(n1, n2):
	return n1 - n2
def mul(n1, n2):
	return n1 * n2
def div(n1, n2):
	return n1 / n2

operation = {
	"+" : add,
	"-" : sub,
	"*" : mul,
	"/" : div
}	
def calculator():
	print(logo)

	n1 = float(input('Enter the first number : \t'))
	for symbol in operation:
		print(symbol)
	should_continue = True

	while should_continue:
		operation_symbol = input('Enter an operation:\t')

		n2 = float(input('Enter the second number : \t'))
		calculation_function = operation[operation_symbol]

		answer = calculation_function(n1, n2)
		if input(f'Type \"y\" to continue calculating with {answer} , or type \"n\" to start new calculation: \t').lower() == 'y':
			n1 = answer
		else:
			should_continue = False
			os.system('cls')
			calculator()
calculator()






