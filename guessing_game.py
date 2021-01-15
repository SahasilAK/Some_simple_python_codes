logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):

	if guess > answer:
		print('Too high')
		return turns-1

	elif guess < answer:
		print('Too low')
		return turns-1

	else:
		print(f"you got it: The answer was {answer}")	

def set_difficulty():
	level = input('Choose difficulty : \"Hard\" or \"Easy\":\n').lower()
	if level == 'hard':
		return HARD_LEVEL_TURNS
	elif level == 'easy':
		return EASY_LEVEL_TURNS
	else:
		print('Wrong Input')	

def game():

	print(logo)
	print('Welcome To The Guessing Game')
	print('I\'m thinking of a number between 1 and 100')
	answer = randint(1,100)
	

	turns = set_difficulty()

	guess = 0
	while guess != answer:
		print(f'You have {turns} attempts remaining to guess to the number.')

		guess = int(input('make a guess :  '))

		turns = check_answer(guess, answer, turns)

		if turns == 0:
			print('You have runn out of attempts')
			return
		elif guess != answer:
			print('Guess Again')
game()

