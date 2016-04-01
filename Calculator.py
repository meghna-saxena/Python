                    #Program for making calculator
#Define functions
#User input of 2 numbers
#Select operation - add, subtract, multiply, divide
#While loop for another calculation

def add(x, y):
     return x + y

def subtract(x, y):
     return x - y

def multiply(x, y):
      return x * y

def divide(x, y):
     return x / y
    
def perform_operation():    
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    
    choice = input("Enter choice: ")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == '1':
       print(num1,"+",num2,"=", add(num1,num2))

    elif choice == '2':
       print(num1,"-",num2,"=", subtract(num1,num2))

    elif choice == '3':
       print(num1,"x",num2,"=", multiply(num1,num2))

    elif choice == '4':
       print(num1,"%",num2,"=", divide(num1,num2))

    else:
       print("Result not found")

print("start of program")
running = True
while running:
    perform_operation()
    user_input = input("Do you want to continue,Y/N?")
    if user_input != "Y":
        running = False
        
print("Finish!")
