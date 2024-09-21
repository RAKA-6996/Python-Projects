import os

# matrix calc
# user input which function to perform in number
# dictionary assign user input
# match cases
# define functions class: 8 functions define
# define visual class : 6 functions read and write

matrix_1 = []  # Matrices for the opeartions as an empty list
matrix_2 = []

# Matrices to store the value of different operations
result_add = [[0,0,0], [0,0,0], [0,0,0]]
result_sub = [[0,0,0], [0,0,0], [0,0,0]]
result_product = [[0,0,0], [0,0,0], [0,0,0]]
result_div = [[0,0,0], [0,0,0], [0,0,0]]
result_trans = [[0,0,0], [0,0,0], [0,0,0]]
result_sqr = [[0,0,0], [0,0,0], [0,0,0]]

class Functions:
    
    def matrix_01(self):
        ''' Takes in input from the user for 1st Matrix'''

        for i in range(1,4):

            row_element = []

            for j in range(1,4):

                elements = int(input(f"Enter {j}th element for row {i} in Matrix 1: "))
                row_element.append(elements)

            matrix_1.append(row_element)
            
    def matrix_02(self):
        ''' Takes in input from the user for 2nd Matrix'''

        for i in range(1,4):

            row_element = []

            for j in range(1,4):

                elements = int(input(f"Enter {j}th element for row {i} in Matrix 2: "))  # Takes input from the user for each element 
                row_element.append(elements)  # Adds the elements into each row

            matrix_2.append(row_element)  # Adds the rows to Matrix
      
    def add_func(self):
        ''' Add function to add 2 Matrix'''

        self.matrix_01() # Calling Matrices in this function to operate
        self.matrix_02()
        
        for i in range(0,3):

            for j in range(0,3):

                result_add[i][j] = matrix_1[i][j] + matrix_2[i][j]  # This line adds the Matrix 1 and Matrix 2 and stores the result in result_add Matrix

        print('\n')
        
        for i in result_add:

            print(f"{i}")
            
        print("\nOPEN THE MATRIX VISUALS FILE FOR MORE DETAILS")
        
    def minus_func(self):
        ''' Minus function to subtract 2 Matrix'''

        self.matrix_01()
        self.matrix_02()
        
        for i in range(0,3):

            for j in range(0,3):

                result_sub[i][j] = matrix_1[i][j] - matrix_2[i][j]
                
        print('\n')
        
        for i in result_sub:

            print(f"{i}")
            
        print("\nOPEN THE MATRIX VISUALS FILE FOR MORE DETAILS") 
        
    def product_func(self):
        ''' Product function to multiply 2 Matrix'''

        self.matrix_01()
        self.matrix_02()
        
        for i in range(0,3):

            for j in range(0,3):

                result_product[i][j] = matrix_1[i][j] * matrix_2[i][j]
                
        print('\n')
        
        for i in result_product:

            print(f"{i}")
            
        print("\nOPEN THE MATRIX VISUALS FILE FOR MORE DETAILS")
        
    def div_func(self):
        ''' Divide function to divide 2 Matrix'''

        self.matrix_01()
        self.matrix_02()
        
        for i in range(0,3):

            for j in range(0,3):

                result_div[i][j] = matrix_1[i][j] / matrix_2[i][j]
                
        print('\n')
        
        for i in result_div:

            print(f"{i}")
            
        print("\nOPEN THE MATRIX VISUALS FILE FOR MORE DETAILS")
         
    def trans_func(self):
        ''' Transpose function to swap the rows and columns of one particular matrix'''

        self.matrix_01()  # Only Matrix 1 is called
        
        for i in range(0,3):

            for j in range(0,3):

                result_trans[j][i] = matrix_1[i][j]  # Interchanged the rows with columns and vice versa
                
        print('\n')
        
        for i in result_trans:

            print(f"{i}")
            
        print("\nOPEN THE MATRIX VISUALS FILE FOR MORE DETAILS")
        
    def sqr_func(self):
        ''' Square function to square each element of particular matrix'''

        self.matrix_01()
        
        for i in range(0,3):

            for j in range(0,3):

                result_sqr[i][j] = matrix_1[i][j] * matrix_1[i][j]  # Mutliplying the matrix by itself

        print('\n')

        for i in result_sqr:

            print(f"{i}")
            
        print("\nOPEN THE MATRIX VISUALS FILE FOR MORE DETAILS")
        
obj1 = Functions()  # Created the obj1 object of class Function()

os.chdir("C:/Users/malay/Documents/Github/Python-Projects")  # Directory changed

class Visuals:
    
    def __init__(self, instance):
        ''' Creating Constructor method to intialize object for this class and to access the Functions() class'''
        self.instance = instance
    
    def add_func_printer(self):
        ''' Prints the result of add operation in MatrixVisuals text file'''

        with open("MatrixVisuals.txt", 'w') as f:
            f.write("Matrix 1:\n")

            for row in matrix_1:
                f.write(f"{row}\n")
            f.write("\n")
            f.write("+\n")
            f.write("\n")

            f.write("Matrix 2:\n")

            for row in matrix_2:
                f.write(f"{row}\n")
            f.write("\n")
            f.write("=\n")
            f.write("\n")

            f.write("Result:\n")

            for row in result_add:
                f.write(f"{row}\n")
            f.write("\n")
            
    def sub_func_printer(self):
        ''' Prints the result of subtract operation in MatrixVisuals text file'''
        with open("MatrixVisuals.txt", 'w') as f:
            f.write("Matrix 1:\n")

            for row in matrix_1:
                f.write(f"{row}\n")
            f.write("\n")
            f.write("-\n")
            f.write("\n")

            f.write("Matrix 2:\n")

            for row in matrix_2:
                f.write(f"{row}\n")
            f.write("\n")
            f.write("=\n")
            f.write("\n")

            f.write("Result:\n")

            for row in result_sub:
                f.write(f"{row}\n")
            f.write("\n")
            
    def product_func_printer(self):
        ''' Prints the result of product function in MatrixVisuals text file'''

        with open("MatrixVisuals.txt", 'w') as f:
            f.write("Matrix 1:\n")

            for row in matrix_1:
                f.write(f"{row}\n")
            f.write("\n")
            f.write("*\n")
            f.write("\n")

            f.write("Matrix 2:\n")

            for row in matrix_2:
                f.write(f"{row}\n")
            f.write("\n")
            f.write("=\n")
            f.write("\n")

            f.write("Result:\n")

            for row in result_product:
                f.write(f"{row}\n")
            f.write("\n")
            
    def div_func_printer(self):
        '''Prints the divide result into the MatrixVisuals text file '''

        with open("MatrixVisuals.txt", 'w') as f:
            f.write("Matrix 1:\n")

            for row in matrix_1:
                f.write(f"{row}\n")
            f.write("\n")
            f.write("/\n")
            f.write("\n")

            f.write("Matrix 2:\n")

            for row in matrix_2:
                f.write(f"{row}\n")
            f.write("\n")
            f.write("=\n")
            f.write("\n")

            f.write("Result:\n")

            for row in result_div:
                f.write(f"{row}\n")
            f.write("\n")
            
    def trans_func_printer(self):
        ''' Prints the result of Transpose function into MatrixVisuals text file'''

        with open("MatrixVisuals.txt", 'w') as f:
            f.write("Matrix 1's Transpose:\n")

            for row in matrix_1:
                f.write(f"{row}\n")
            f.write("\n")
            f.write("=\n")
            f.write("\n")

            f.write("Result:\n")

            for row in result_trans:
                f.write(f"{row}\n")
            f.write("\n")
            
    def sqr_func_printer(self):
        ''' Prints the result of square function into MatrixVisuals text file'''

        with open("MatrixVisuals.txt", 'w') as f:
            f.write("(Matrix 1)^2:\n")

            for row in matrix_1:
                f.write(f"{row}\n")
            f.write("\n")
            f.write("=\n")
            f.write("\n")

            f.write("Result:\n")

            for row in result_sqr:
                f.write(f"{row}\n")
            f.write("\n")
            
obj2 = Visuals(obj1)  # Created the obj2 object and used the obj1 as an instance to access the Function class in Visuals() class

print("WELCOME TO MATRIX CALCULATOR\nPERFORM CALCULATION HERE AND GET OUTPUT IN A TEXT FILE!")

user_input = int(input("Enter which operation do you want to perform:\nType 0 for Plus\nType 1 for Minus\nType 2 for Product\nType 3 for Division\nType 4 for Transpose\nType 5 for Squaring each element\nType 6 to Exit\nEnter Here: "))

if user_input < 0 or user_input > 6:  # Setting the range of input for users

    raise IndexError("Out of Bound!! BAKCHODI MAT KAR LO*E")
    
else:

    match user_input:  # Switch Cases connected with user_input
            
        case 0:
            obj1.add_func()
            obj2.add_func_printer()
        case 1:
            obj1.minus_func()
            obj2.sub_func_printer()
        case 2:
            obj1.product_func()
            obj2.product_func_printer()
        case 3:
            obj1.div_func()
            obj2.div_func_printer()
        case 4:
            obj1.trans_func()
            obj2.trans_func_printer()
        case 5:
            obj1.sqr_func()
            obj2.sqr_func_printer()
        case 6:
            exit()