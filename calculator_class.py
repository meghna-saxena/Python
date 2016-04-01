#Create calculator class
#Create constructor
#Define functions
#Select operation - add, subtract, multiply, divide
#User input of 2 numbers
#Print result


class calculator:
    
    def __init__(self):
        print("calculator initialized")

    def addition(self, x, y):
        added = x + y

    def subtraction(self, x, y):
        subtracted = x - y

    def multiplication(self, x, y):
        multiplied = x * y

    def division(self, x, y):
        divided = x % y

    def perform_operation(self):
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        choice = input("Enter choice of operation: ")

        x = int(input("Give the first no. ?"))
        y = int(input("Give the second no. ?"))

        if choice == '1':
                addition(x,y)
                print(added)

        elif choice == '2':
                subtraction(x,y)
                print(subtracted)

        elif choice == '3':
                multiplication(x,y)
                print(multiplied)

        elif choice == '4':
                division(x,y)
                print(divided)

        else:
            print("Result not found")

cal = calculator()
cal.perform_operation()
