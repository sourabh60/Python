import os
#HINT: You can call clear() to clear the output in the console.
from art import logo

bids={}
bidding_finished=False

def find_highest_bidder(bidding_record):
  highest_bid=0
  winner=''
  for bidder in bidding_record:
    bid_amount= bidding_record[bidder]
    if bid_amount> highest_bid:
      highest_bid=bid_amount
      winner=bidder
  print(f"The highest bidder is {winner} with a bid amount of ${bid_amount}")


while not bidding_finished:

  name=input("What is your name?:")
  price=int(input("What\'s your bid?: $"))
  bids[name]=price
  should_continue=input("Are there any other bidders? Type 'yes' or 'no'.")
  if should_continue == 'no':
    bidding_finished=True
    find_highest_bidder(bids)
  elif should_continue == 'yes':
    os.system('cls')




  
