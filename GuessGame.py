# Guess Game

''' user input
tell low or high: match user input with random number
if low low
if high high'''

import random
print('Welcome to Guess Game\n')

random_number = random.randint(0, 100)

life = 13

while life > 0:
    
    user = int(input("Enter a number between 0 to 100: "))
    if 0 < user < 100:
        
        if user == random_number:
            print(f'\nCongratulations! You guessed the right number {user}')
            break
        elif user > random_number:
            print('\nToo High. Try Again!')
            life -= 1
        else:
            print('\nToo Low. Try Again!')
            life -= 1
        print(f'Your life {life}')
    
    else:
        raise ValueError('Invalid input! Guess number between 0 to 100.')
