"""
This project is me trying to make a basic calculator program,
which is addition, subtraction, multiplication and division.
"""

#The definition of all functions starts here
def keep_window_open():
    user_input = input("Press any key to exit...")

#Defines addition function
def add(num1,num2):
    ans = num1 + num2
    while True:
        confirm = (input("Do you want to include another number in the calculation? ")).lower()
        if confirm == "y" or confirm == "yes" or confirm == "yeah" or confirm == "yh":
            xtra_num = int(input("What is the number? "))
            ans += xtra_num
        elif confirm == "n" or confirm == "no" or confirm == "nope" or confirm == "nah":
            break
        else:
            print("Invalid data inputted")

    print("The final answer is %s" % str(ans))

#Defines multiplication function
def multiply(num1,num2):
    ans = num1 * num2
    while True:
        confirm = (input("Do you want to include another number in the calculation? ")).lower()
        if confirm == "y" or confirm == "yes" or confirm == "yeah" or confirm == "yh":
            xtra_num = int(input("What is the number? "))
            ans *= xtra_num
        elif confirm == "n" or confirm == "no" or confirm == "nope" or confirm == "nah":
            break
        else:
            print("Invalid data inputted")

    print("The final answer is %s" % str(ans))

#Defines subtraction function
def subtract(num1,num2):
    ans = num1 - num2
    while True:
        confirm = (input("Do you want to include another number in the calculation? ")).lower()
        if confirm == "y" or confirm == "yes" or confirm == "yeah" or confirm == "yh":
            xtra_num = int(input("What is the number? "))
            ans -= xtra_num
        elif confirm == "n" or confirm == "no" or confirm == "nope" or confirm == "nah":
            break
        else:
            print("Invalid data inputted")

    print("The final answer is %s" % str(ans))

#Defines division function
def divide(num1,num2):
    ans = num1 / num2
    while True:
        confirm = (input("Do you want to include another number in the calculation? ")).lower()
        if confirm == "y" or confirm == "yes" or confirm == "yeah" or confirm == "yh":
            xtra_num = int(input("What is the number? "))
            ans /= xtra_num
        elif confirm == "n" or confirm == "no" or confirm == "nope" or confirm == "nah":
            break
        else:
            print("Invalid data inputted")

    print("The final answer is %s" % str(ans))

#The defintion of all functions ends here

#The actual sequence of the program starts here
name = input("What is your name? ")
welcome_message = "Hi %s , this is a basic calculator program that can only carry out the 4 basic math operations" % (name)
print (welcome_message)

#Ensures user knows the correct type of data to input
print("""'+', 'add' or 'addition' for addition operation
'-', 'subtract' or 'subtraction' for subtraction operation
'*', 'multiply' or 'multiplication' for multiplication operation
'/', 'divide' or 'division' for division operation
""")

while True:
    operation = (input("What mathematical operation do you want to carry out? ")).lower()

    if (operation == "+" or operation == "add" or operation == "addition"):
        num1 = int(input("What is your first number? "))
        num2 = int(input("What is your second number? "))
        add(num1,num2)
        contd = (input("Would that be all for this session? ")).lower()
        if (contd == "y" or contd == "yes" or contd == "yeah" or contd == "yh"):
            keep_window_open()
            break
        elif (contd == "n" or contd == "no" or contd == "nope" or contd == "nah"):
            continue
    elif (operation == "*" or operation == "multiply" or operation == "multiplication"):
        num1 = int(input("What is your first number? "))
        num2 = int(input("What is your second number? "))
        multiply(num1,num2)
        contd = (input("Would that be all for this session? ")).lower()
        if (contd == "y" or contd == "yes" or contd == "yeah" or contd == "yh"):
            keep_window_open()
            break
        elif (contd == "n" or contd == "no" or contd == "nope" or contd == "nah"):
            continue
    elif (operation == "-" or operation == "subtract" or operation == "subtraction"):
        num1 = int(input("What is your first number? "))
        num2 = int(input("What is your second number? "))
        subtract(num1,num2)
        contd = (input("Would that be all for this session? ")).lower()
        if (contd == "y" or contd == "yes" or contd == "yeah" or contd == "yh"):
            keep_window_open()
            break
        elif (contd == "n" or contd == "no" or contd == "nope" or contd == "nah"):
            continue
    elif (operation == "/" or operation == "divide" or operation == "division"):
        num1 = int(input("What is your first number? "))
        num2 = int(input("What is your second number? "))
        divide(num1,num2)
        contd = (input("Would that be all for this session? ")).lower()
        if (contd == "y" or contd == "yes" or contd == "yeah" or contd == "yh"):
            keep_window_open()
            break
        elif (contd == "n" or contd == "no" or contd == "nope" or contd == "nah"):
            continue
    else:
        print("invalid data inputted")
