#netsh wlan show profile name="NETWORK_NAME" key=clear

import os
import subprocess

os.chdir("C:/Users/malay/Documents/Github/Python-Projects")

user_input_sym = input('Select which symbol to use for design printing\nEnter: ')

file_path_selection = 'Select.txt'

os.name == 'nt'
subprocess.Popen(['notepad.exe', file_path_selection])

user_input_design = int(input("Enter the number for the design you want to print\nEnter: "))

input_times = int(input("How many times do you want to print the design\nEnter: "))

print(f"You selected design number {user_input_design} to print it {input_times} times, with the {user_input_sym} symbol.")

class Design():
    
    size = int(input('Enter a size between 10-30 here: '))
    
    def pyramid(self):
        
        if user_input_design == 1:
            for i in range(input_times):
                for j in range(1,self.size+1):
                    print(' ' * (self.size-j), end='')
                    print(j*user_input_sym, end='')
                    print((j-1)*user_input_sym)
                    
    def inverted_pyramid(self):
                
        if user_input_design == 2:
            for i in range(input_times):
                for j in range(1, self.size+1):
                    print(' ' * (j-1),end='')
                    print((self.size-j) * user_input_sym, end='')
                    print((self.size-(j+1))*user_input_sym)
                    
    def diamond(self):
                
        if user_input_design == 3:
            for i in range(input_times):
                for j in range(1, int((self.size+1)/2)):
                    print(' ' * (self.size-j), end='')
                    print(j*user_input_sym, end='')
                    print((j-1) * user_input_sym)
                    
                for g in range(1, int((self.size-1)/2)):
                    print(' ' * int((self.size+1)/2 + g), end='')
                    print((int((self.size-1)/2)-g)*user_input_sym, end='')
                    print((int((self.size-1)/2)-g-1)*user_input_sym)
                                   
    def right_tri(self):
        
        if user_input_design == 4:
            for i in range(input_times):
                for j in range(1, self.size):
                    print(j*user_input_sym)
                    
    def hr_glass(self):
                
        if user_input_design == 5:
            for i in range(input_times):
                for j in range(1, self.size):
                    print((self.size-j)*user_input_sym)
                    
                for g in range(2, self.size):
                    print(g*user_input_sym)
                    
    def hollow_diamond(self):
                
        if user_input_design == 6:
            for i in range(input_times):
                for j in range(1, self.size):
                    print(' ' * (self.size-j), end='')
                    print(user_input_sym, end='')
                    print(' ' * ((j-1)+(j-2)), end='')
                    if j==1:
                        print()
                    else:
                        print(((j+1)-(j))*user_input_sym)
                    
            
                for y in range(1, self.size-1):
                   print(' ' * (y+1), end='')
                   print(user_input_sym, end='')
                   if y == (self.size-2):
                       print()
                   else:
                       print(' ' * ((self.size-y-2)+(self.size-y-3)), end='')
                       print(user_input_sym)
obj = Design()

output_dict = {1:obj.pyramid(), 2:obj.inverted_pyramid(), 3:obj.diamond(), 4:obj.right_tri(), 5:obj.hr_glass(), 6:obj.hollow_diamond()}

if user_input_design in output_dict:
    print()
else:
    print("Invalid Input!")