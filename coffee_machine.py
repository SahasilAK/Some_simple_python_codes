
# Data for coffee machine
logo ="""

        /~~~~~~~~~~~~~~~~~~~/|
       /              /######/ / |
      /              /______/ /  |
     ========================= /||
     |_______________________|/ ||
      |  \****/     \__,,__/    ||
      |===\**/       __,,__     ||    
      |______________\====/%____||
      |   ___        /~~~~\ %  / |
     _|  |===|===   /      \%_/  |
    | |  |###|     |########| | /
    |____\###/______\######/__|/
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
cup = """

  .-~~-.
,|`-__-'|
||      |
`|      | 
  `-__-'

"""


MENU = {
	"espresso": {
		"ingredients": {
			"water": 50,
			"coffee": 18,
		},
		"cost": 1.5,
	},
	"latte": {
		"ingredients": {
			"water": 200,
			"milk": 150,
			"coffee": 24,
		},
		"cost": 2.5,
	},
	"cappuccino": {
		"ingredients": {
			"water": 250,
			"milk": 100,
			"coffee": 24,
		},
		"cost": 3.0,
	}
}

profit = 0

resources = {

"water" : 300,
"milk" : 100,
"coffee" : 24
}

choices = {"1" : "espresso",
"2" : "latte",
"3" : "cappuccino"}




def is_resources_sufficient(order_ingrediants):
	for item in order_ingrediants:
		if order_ingrediants[item] > resources[item]:
			print(f'Sorry there is not enough {item} ')
			return False
		return True







def process_coin():
	print('Please Insert Coins')
	total = int(input('how many quaters?: '))*0.25
	total += int(input('how many dimes?: '))*0.10
	total += int(input('how many nickels?: '))*0.05
	total += int(input('how many pennies?: '))*0.01
	return total

def is_transaction_successful(money_received, drink_cost):
	if money_received >= drink_cost:
		change = round(money_received - drink_cost, 2)

		print (f'Here is your  ${change} in change')
		global profit 
		profit += drink_cost
		return True
	else:
		print('Sorry not enough money. Money is refunded ')
		return False




def make_coffee(drink_name, order_ingrediants):
	for item in order_ingrediants:
		resources[item] -= order_ingrediants[item]
	print('\n')
	print(cup)
	print(f'Here is your {drink_name}☕ enjoy')
	print(logo)




print(logo)
is_on = True

while is_on:

	user_choice = input("What would you like?\n 1 - ☕  Espresso \n 2 - ☕  Latte \n 3 - ☕  Cappuccino\n9 - Report \n0 - Turn Off \n--->")



	if user_choice == "0":
		is_on = False

	elif user_choice == "9":
		print('~~~~~~~~~~~~~~~~~~~~~~~~~~')
		print(f'Water : {resources["water"]}ml') 
		print(f'Milk : {resources["milk"]}ml')
		print(f'Coffee : {resources["coffee"]}g')
		print(f'Money : ${profit}')   
		print('~~~~~~~~~~~~~~~~~~~~~~~~~~')

	else:
		if user_choice in choices.keys():
	
			choice = choices[user_choice]


			drink = MENU[choice]
			print(f'Price : ${drink["cost"]}')
			if is_resources_sufficient(drink["ingredients"]):
				payment = process_coin()
				if is_transaction_successful(payment, drink["cost"]):
					make_coffee(choice, drink["ingredients"])

		else:
			print('\n')
			print('Enter a valid choice')
			print(logo)






		



