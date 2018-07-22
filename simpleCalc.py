# A simple calculator with menu options to perform calculations

def addition (n, m):
    return n + m

def subtraction (n, m):
    return n - m

def multiplication (n, m):
    return n * m

def division (n, m):
    return n / m

def goAgain():
    c = input("Would you like to perform another operation? y/n: ")
    if c == "y":
        simpleCalc()
    if c == "n":
        print ("Thanks for using simple calc")
    if c != "y" and c != "n":
        print ("Please enter y to continue or n to quit")

def simpleCalc():
    print ("Welcome to Simple Calc")
    while True:
        print ("Press 1 to add two numbers")
        print ("Press 2 to subtract two numbers")
        print ("Press 3 to divide two numbers")
        print ("Press 4 to multiply two numbers")
        op = int(input("Which operation would you like to perform?  "))
        if op == 1:
            a = int(input("Please enter first number to be added: "))
            b = int(input("Please enter second number to be added: "))
            print ("The sum of " , a , " and " , b , " is: " , addition(a, b))
        elif op == 2:
            a = int(input("Please enter number to be subtracted from: "))
            b = int(input("Please enter number to subtract from first number: "))
            print ("Result of ", a ,  " minus " , b ," is: " , subtraction (a, b))
        elif op == 3:
            a = int(input("Please enter the dividend: "))
            b = int(input("Please enter the divisor: "))
            print (a, " divided by ", b , " is: " , division(a, b))
        elif op == 4:
            a = int(input("Please enter first number to be multiplied: "))
            b = int(input("Please enter the second number to be multiplied: "))
            print (a, " mulitplied by " , b , " is: ", multiplication(a,b))
        else:
            print("Must be number between 1 & 4")
            continue
        goAgain()
        break





