# Rock Paper Sci Game
'''Rock > Scissor
   Scissor > Paper
   Paper > Rock'''

import random
choices = ['rock', 'paper', 'scissors']

print("Rock\nPaper\nScissors.")
user_points = 0
computer_points = 0

for i in choices:
    computer_choice = random.choice(choices).lower()
    user_choice = input("Enter here: ").lower()
    
    if user_choice in choices:
        
        if user_choice == computer_choice:
            print('\nIts a tie')
        elif user_choice == 'rock' and computer_choice == 'paper' or user_choice == 'paper' and computer_choice == 'scissors' or user_choice == 'scissors' and computer_choice == 'rock':
            print('\nYou lose this round!')
            computer_points += 1
        else:
            print('\nYou win this round!')
            user_points += 1
            
        print(f"Computer Points = {computer_points}")
        print(f"Your Points = {user_points}\n")
        print(f"Computer chose '{computer_choice}'")
    else:
        raise ValueError('Invalid Input!')
        
if computer_points > user_points:
    print("You Lose The Game!")
else:
    print("You Won The Game!")
    