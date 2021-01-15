print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Tresure Island")
print("Your missin is to find the tresure")
a = input('You are at a cross road. Where do you want to go? "left" or "right"\n').lower()

if a == "left":
    b = input('You come at a lake. There is an island in the  middle of the lake. Type "wait" tot wait fo the boat or Type "swim" to swim across ?\n').lower()
   
    if b == "wait":
         c = input('You arrived at th island unharmed. There is  a house with 3 doors. One red, one blue and one yellow. Which door do you choose?\n').lower()
        
         if c == "blue":
         	print('Eaten by beasts. Game OVer.')
       
         elif c == "yellow":
         	print('!!!!!You Win!!!!!')
       
         elif c == "red":
          	print('Burned by fire. Game Over')
        
         else:
          	print('Game Over')
    
    else:
         print("Attack by trout. Game Over.")

else:
	print("FAll into a hole. Game Over")


