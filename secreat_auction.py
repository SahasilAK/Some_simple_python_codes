

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)


import os

bids = {}

def highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""

  for bidder in bidding_record:

    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder

  print(f'The winner is {winner} with the bid of ${highest_bid}')









should_continue = False

while not should_continue:

  name = input('Enter Your Name : \n')

  bid = int(input('Enter Your Bid :\n$'))

  bids[name] = bid

  next_person = input('Are there any other bidder Yes or No :\n').lower()

  if next_person == "no":
    should_continue = True
    highest_bidder(bids)


  elif next_person == "yes":
    os.system("cls")


