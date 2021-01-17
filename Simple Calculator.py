"""This is the code for a simple calculator
Using Python 3.9.1 by  @CharlesNorris
the 17/01/2021"""

def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Welcome to the calculator")
print("Select Operation")
print("1-Add")
print("2-Substract")
print("3-Multiply")
print("4-Divide")

while True:
    choice = input("Enter your choice 0, 1, 2, 3, 4 :")

    if choice in ('1', '2', '3', '4'):
        num1= float(input("Enter the first number :"))
        num2 = float(input("Enter  the  second number :"))

        if choice == '1':
            print(num1," +", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", substract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, '/',num2, "=", divide(num1, num2))
            break
        else :
            print(f"Invalid Input")