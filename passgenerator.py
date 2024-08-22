#PassWord Generator

import string
import random

all_charc = string.ascii_letters + string.digits + string.punctuation

print('\nPasssWord Generator\nGenerally, strong passwords are between 12 to 15 characters.\nSelect the length between 12 to 15 below.\n')
user_input = int(input("Enter here: "))
print("We will provide you 10 strong passwords of your chosen length.\n")

for i in range(10):
    
    if 12<=user_input<=15:
    
        match user_input:
            
            case 12:
                main_string = ''.join(random.choice(all_charc) for _ in range(12))
                print(main_string)
            case 13:
                main_string = ''.join(random.choice(all_charc) for _ in range(13))
                print(main_string)
            case 14:
                main_string = ''.join(random.choice(all_charc) for _ in range(14))
                print(main_string)
            case 15:
                main_string = ''.join(random.choice(all_charc) for _ in range(15))
                print(main_string)
                
    elif user_input>15 or user_input<12:
        raise ValueError('Invalid input! Select the length of password between 12 to 15!')
        
    else:
        raise ValueError('The input must be an integer!')
            