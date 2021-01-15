import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
com_choice = random.randint(0, 2)
if user_choice >= 3 or user_choice < 0:
	print('Enter a Valid number')
else:	
    print(game_images[user_choice])

    
    print(game_images[com_choice])


    if user_choice == 0 and com_choice == 2:
 	      print('!!You Win!!')
    elif com_choice == 0 and user_choice == 2:
  	       print('!!You Lose!!')
    elif com_choice > user_choice:
	       print('!!You Lose!!')
    elif user_choice > com_choice:
	       print('!!You WIn!!')
    elif com_choice == user_choice:
	        print("!!ITs A Draw!!")

