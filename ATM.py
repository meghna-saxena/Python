balance = 10000

def perform_operation():
    print ("1)Balance ")
    print ("2)Withdraw ")
    print ("3)Deposit ")
    print ("4)Quit ")

    option = int(input("Enter Option: "))

    if option == 1:
        print("Balance  Rs. ",balance)

    elif option == 2:
        print("Balance  Rs.  ",balance)
        withdraw = int(input("Enter Withdraw amount Rs. "))

        if withdraw  < balance:
            foreward_balance = (balance-withdraw)
            print("foreward_balance  Rs. ",foreward_balance)
        elif withdraw > balance:
            print("Balance unavailable")
        else:
            print("None withdraw made")

    elif option == 3:
        print("Balance  Rs. ",balance)
        deposit = int(input("Enter deposit amount Rs. "))

        if deposit > 0:
            foreward_balance = (balance+deposit)
            print("foreward_balance  Rs. ",foreward_balance)

        else:
            print("None deposit made")

    elif option == 4:
            print("Thanks for using our ATM service")

    else:
        print ("Result Invalid") 


print("Start of the ATM Program")
running = True
while running:
    perform_operation()
    user_input = input("Do you want to continue,Y/N?")
    if user_input != "Y":
        running = False
        
