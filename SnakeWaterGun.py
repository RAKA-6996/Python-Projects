import random

main_matrix = [
   # S W G 
    [0,1,-1],#Snake
    [-1,0,1],#Water
    [1,-1,0]#Gun
]

# 0 - indicates DRAW, 1 - indicates WIN, -1 - indicates LOSE

choices = {'S':0, 'W':1, 'G':2} # Adjust accoring to the matrice's indices

def computer_choice():
    return random.choice(['S','W','G']) # Computer chooses from the list of options

def main():
    player_choice = input("Choose:\nS for Snake\nW for Water\nG for Gun\nEnter: ").upper() # Player input

    if player_choice not in choices: # Checks whether input is valid or not
        print("Invalid input! Select from the options given.")
        return

    computer = computer_choice() # Stores the computer choice in the form of variable
    print(f"Computer chose: {computer}")

    result = main_matrix[choices[player_choice]][choices[computer]] # Evaluates the choice's dictionary and then search for exact indices in the main_matrix

    if result == 1: # Displays the result
        print("You Won!")
    elif result == 0:
        print("Draw")
    else:
        print("You Lost")

main()