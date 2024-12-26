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
result_product = [[0,0,0], [0,0,0],[0,0,0]]
result_div = [[0,0,0], [0,0,0], [0,0,0]]
result_trans = [[0,0,0], [0,0,0], [0,0,0]]
result_power = [[0,0,0], [0,0,0], [0,0,0]]
result_inverse = [[0,0,0],[0,0,0],[0,0,0]]

class Functions:
    
    def matrix_01(self):
        ''' Takes in input from the user for 1st Matrix'''

        for i in range(1,4):

            row_element = []

            for j in range(1,4):

                elements = float(input(f"Enter {j}th element for row {i} in Matrix 1: "))
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

        row_A = len(matrix_1)
        col_A = len(matrix_1[0])
        col_B = len(matrix_2[0])

        for i in range(row_A):
            for j in range(col_B):
                for k in range(col_A):
                    result_product[i][j] += matrix_1[i][k] * matrix_2[k][j]

        for row in result_product:
            print(row)

        print("\nOPEN THE MATRIX VISUALS FILE FOR MORE DETAILS")
        
    def div_func(self):
        ''' Divide function to divide 2 Matrix'''

        self.matrix_01()
        self.user_num = int(input("Enter a number from which you want to divide the Matrix: "))
        
        for i in range(0,3):

            for j in range(0,3):

                result_div[i][j] = matrix_1[i][j] / self.user_num
                
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
        
    def power_func(self):
        ''' Powers each element of particular matrix'''

        self.matrix_01()
        self.n = int(input("Enter the power number for operation: "))

        for i in range(0,3):

            for j in range(0,3):

                result_power[i][j] = (matrix_1[i][j]) ** self.n # Mutliplying the matrix by itself

        print('\n')

        for i in result_power:

            print(f"{i}")
            
        print("\nOPEN THE MATRIX VISUALS FILE FOR MORE DETAILS")

    def inverse_func(self):
        '''Computes the Inverse of a matrix'''

        self.matrix_01()

        a = matrix_1[0][0]
        b = matrix_1[0][1]
        c = matrix_1[0][2]
        d = matrix_1[1][0]
        e = matrix_1[1][1]
        f = matrix_1[1][2]
        g = matrix_1[2][0]
        h = matrix_1[2][1]
        i = matrix_1[2][2]

        det_A = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

        if det_A == 0:
            raise ValueError("The matrix is singular and no inverse of the matrix exists.")
        
        cofactors = [
                     [(e * i - f * h), -(b * i - c * h), (b * f - c * e)], 
                     [-(d * i - f * g), (a * i - c * g), -(a * f - c * d)],
                     [(d * h - e * g), -(a * h - b * g), (a * e - b * d)]
                     ]
        
        adjugate = [[cofactors[j][i] for j in range(3)] for i in range(3)]

        global result_inverse
        result_inverse = [[adjugate[i][j] / det_A for j in range(3)] for i in range(3)]

        print('\n')

        for k in result_inverse:
            print(f"{k}")

        print("\nOPEN THE MATRIX VISUALS FILE FOR MORE DETAILS")
    
    @property
    def value_returner(self):
        return self.user_num
    
    @property
    def power_returner(self):
        return self.n

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
            f.write(f"{obj1.value_returner}")
            f.write("\n")
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
            
    def power_func_printer(self):
        ''' Prints the result of powered elements into MatrixVisuals text file'''

        with open("MatrixVisuals.txt", 'w') as f:
            f.write("(Matrix 1)^2:\n")

            for row in matrix_1:
                f.write(f"{row}\n")
            f.write("\n")
            f.write(f"To the power ^{obj1.power_returner}")
            f.write("\n")
            f.write("=\n")
            f.write("\n")

            f.write("Result:\n")

            for row in result_power:
                f.write(f"{row}\n")
            f.write("\n")
    
    def inverse_func_printer(self):
        ''' Prints the result of inverse matrix into MatrixVisuals text file'''

        with open("MatrixVisuals.txt", 'w') as f:
            f.write("Inverse of Matrix 1:\n")

            for row in matrix_1:
                f.write(f"{row}\n")
            f.write("\n")
            f.write("=\n")
            f.write("\n")

            f.write("Result:\n")
            
            for row in result_inverse:
                f.write(f"{row}\n")
            f.write("\n")
            
obj2 = Visuals(obj1)  # Created the obj2 object and used the obj1 as an instance to access the Function class in Visuals() class

print("WELCOME TO MATRIX CALCULATOR\nPERFORM CALCULATION HERE AND GET OUTPUT IN A TEXT FILE!")

user_input = int(input("Enter which operation do you want to perform:\nType 0 for Plus\nType 1 for Minus\nType 2 for Product\nType 3 for Division\nType 4 for Transpose\nType 5 for to the power of each element\nType 6 to compute inverse\nType 7 to Exit\nEnter Here: "))

if user_input < 0 or user_input > 7:  # Setting the range of input for users

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
            obj1.power_func()
            obj2.power_func_printer()
        case 6:
            obj1.inverse_func()
            obj2.inverse_func_printer()
        case 7:
            exit()