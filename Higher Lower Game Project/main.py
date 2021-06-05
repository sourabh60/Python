from art import logo,vs
import random
import os
from game_data import data
game_should_contine= True


# Format account data into printable format.
def format_data(account):
  account_name=account["name"]
  account_desc=account["description"]
  account_country=account["country"]
  return f"{account_name},{account_desc} from {account_country}"

def check_answer(guess,a_followers, b_followers):
  if a_followers>b_followers:
    return guess=="a"
  else:
    return guess=="b"

print(logo)
# Make B become the next A.
account_b=random.choice(data)
score=0
  # Generate a random account from the game data.
# Make game repeatable.
while game_should_contine:
  account_a=account_b
  account_b=random.choice(data)
  
  while account_a == account_b:
    account_b=random.choice(data)

  print(f"Compare A: {format_data(account_a)}.")
  print(vs) # Add art.
  print(f"Against B: {format_data(account_b)}.")


  # Ask user for a guess.
  guess=input("Who has more followers? Type 'A' or 'B': ").lower()

  # Check if user is correct.

  ## Get follower count.
  a_follower_count=account_a["follower_count"]
  b_follower_count=account_b["follower_count"]
  is_correct=check_answer(guess,a_follower_count,b_follower_count)
  os.system("cls")
  print(logo)
# If Statement
  if is_correct:
    score+=1  # Score Keeping.
    print(f"You're right! Current score: {score}")
  else:
    game_should_contine=False
    print(f"That's wrong! Final score {score}")









