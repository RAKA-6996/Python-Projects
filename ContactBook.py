# CONTACT BOOK 
# BEST PROJECT TILL NOW

import os
os.chdir("C:/Users/malay/Documents/Github/Python-Projects")  # Changes the current directory to mentioned one.

print('Welcome to Contact Book!\n')

opt_choose = {0:'View', 1:'Add', 2:'Delete', 3:'Exit'}    # Options for USER

print(f'Select Your Desired Option to view or make changes to contact book:\n0 to {opt_choose[0]}\n1 to {opt_choose[1]}\n2 to {opt_choose[2]}\n3 to {opt_choose[3]}')

user = int(input("\nEnter your option here: "))

def check_duplis(name,number):      # This function is linked to Add() function, it checks if there is any duplicate names and numbers.
    with open('contact.txt', 'r') as files:
        lines = files.readlines()
        
    for line in lines:
        if name in line and number in line:  # This statement checks if the global variable: name and number, exists in file.
            return True   # If exists True
    return False   # If not False

def name_exist(name1,lines):   # This function is linked to Delete() function, it checks if the contact to delete exists in file or not.
    for line in lines:
        if name1 in line:
            return True   # If yes True
    return False   # If not False

def update():   # This function updates the file after manipulating it. 
    space_remover()
    
    f = open('contact.txt', 'r')
    contact_list = f.read()   # Reads the content of the file and store it in contact_list variable.
    print(contact_list)   # Prints the variable
    f.close()    
    
def space_remover():          # This function removes the extra whitespaces in between the lines.
    with open('contact.txt','r') as files:
        lines = files.readlines()         # Reads the lines present in file
        
    non_blank = [line for line in lines if line.strip()]         # This statement removes the whitespaces present in file and stores it in variable.
    
    with open('contact.txt','w') as files:
        for line in non_blank:
           files.write(line)       # Writes the updated lines in the file.

def View():          # This function is used to View the contact book.
    print("\nYou selected to view the contact book.")
    
    space_remover()
    f = open('contact.txt','r')
    file = f.read().strip()
    
    if len(file) == 0:   # Checks the length of the Contact Book
        print("\nContact Book is empty, try adding some contacts to view here.")
    
    else:
        print(file)
        f.close()
    
def Add():          # This function is used to add new contacts to the Book.
    print("\nYou selected to add a new contact to book.")
    
    global name
    global number
    
    print("Enter Name and Phone Number of the person you want to add below.\n")
    name = input("Name: ").capitalize()
    number = input("Phone Number: ")

    print("")
    if len(number) != 10:  # Checks whether the entered number is of 10-Digit.
        raise ValueError('Invalid. The length of phone number should be 10-digit only.')
        
    if check_duplis(name, number):   # If the check_duplis function returns True, the if statement will execute. However, if it returns False the if-statement won't execute
        print(f'The name ({name}) and number ({number}) already exists. No changes were made!')
        
    else:
        
        f = open('contact.txt', 'a')
        f.write(f'\n{name} - {number}')
    
        print("The Contact book has been updated.")  
    
def Delete():         # This function is used to delete contacts from the Book.
    print("\nYou selected to delete a contact from the book.")
    
    print('Enter the Name of the Person you want to delete below.\n')
    
    to_delete = input("Enter full Name: ").capitalize()
    
    print("")
    
    if to_delete.isalpha():        # Checks if the input from user contains only alphabets not numbers or special symbols.
        with open('contact.txt', 'r') as file:
            lines = file.readlines()
            
        if name_exist(to_delete, lines):   # If the name_exist function returns True, it will execute the if-statement. If it returns False, else-statement will be executed.
            
            with open('contact.txt', 'w') as file:      
                for line in lines:
                    if to_delete not in line:    # Checks if the to_delete --> name inputed from the user in file or not, if it isn't there it will overwrite the line. If it exists, it won't write it and that name will be deleted.
                        file.write(line)
                    
            print("The Contact book has been updated.")
            update()
        else:         # Throws message, if name_exist function returns False.
            print(f"The name {to_delete} doesn't exist in the contact book.")
    else:         # Throws message, if the value is other than alphabetic.
        raise ValueError(f"The input {to_delete} is INVALID. Try entering a valid name!")
        
if 0 <= user <= 3:   # SWITCH CASES
    match user:
        
        case 0:
            View()
        case 1:
            Add()
            update() 
        case 2:
            Delete()
        case 3:
            exit()
    
else:        # Throws ValueError, if the input isn't choosen from the selected switch cases.
    raise ValueError('Invalid input! Select from the given option.')    
