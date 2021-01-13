#Write a python program (menu driven) that asks for an operation to be performed on two input numbers. 
# Operations are add, subtract, divide, multiply. 
# The program should keep asking for options on new numbers until the user specifies explicitly to exit. 
# Also handle the scenario of divide by zero through exception handling in python.
import math

print(""" Welcome to this calculator program, you can select from one from the operations given below:
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division 
        To continue, press 'y', else press 'n' to exit the calculator""")

option = input()
while option == 'y':
    ch = int(input("Enter your choice of operation"))
    print("Enter the operands")
    a = int(input("Enter operand a: "))
    b = int(input("Enter operand b:"))
    try:
        switcher = {
            1: (a+b),
            2: (a-b),
            3: (a*b),
            4: (a/b)
        }
        switcher.get(ch, "Undefined option")

    except:
        print("Division by zero is not permissible")
    else:
        print("Answer:")
        print(switcher.get(ch, "Undefined option"))


    print("Press 'y' to continue or 'n' to stop the execution")
    option = input()
    if(option == 'n'):
        break



