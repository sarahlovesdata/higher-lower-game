import random
from game_data import data
from art import logo, vs
from replit import clear

#Format the account data into a printable format
#Go into dictionary and pull out value under the key "name" and save it to the variable account name
def format_data(account):
  """Takes the account data and returns the printable format"""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return(f"{account_name}, a {account_descr}, from {account_country}")

#Use an if statement to check if user is correct

def check_answer(guess, followers_a, followers_b):
  """Takes the user guess and follower counts and returns if they got it right"""
  if followers_a > followers_b:
    #return guess == "a" will return true when a is correct. When false, it will return b when b is correct.
    return guess == "a"
  else:
    return guess == "b"
      

def game():
  #Display art
  print(logo)
  score = 0
  game_should_continue = True
  account_a = random.choice(data)
  account_b = random.choice(data)


  while game_should_continue:
    #Generate a random account from the data
    account_a = account_b
    account_b = random.choice(data)
    #Prevent duplicate accounts being displayed
    
    while account_a == account_b:
      account_b = random.choice(data)

      #Calls format data function and passes in account a and account b and prints the output for the game user
      print(f"Compare A: {format_data(account_a)}.")
      print(vs)
      print(f"Against B: {format_data(account_b)}.")

      #Ask user for a guess. Convert to lowercase to prevent issues
      guess = input("Who has more followers? Type 'A' or 'B': ").lower()

      #Get the follower count of each account
      followers_a = int(account_a["follower_count"])
      followers_b = int(account_b["follower_count"])
      #Check if correct
      is_correct = check_answer(guess, followers_a, followers_b)
      
      #Clear progress after each round
      clear()
      print(logo)
      
      #Give user feedback based on their answer (true = correct or false = incorrect). When incorrect, game ends and we print their final scorer
      if is_correct:
        score += 1
        print(f"You're right. Current score: {score}.")
      else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")

game()
    






