#WAP to loop through and print the multiplication table of an input.

print("Hello Raj")
#function begins
def print_multiplication_table():
    num = int(input("Write multiplication table of ?"))

    for i in range(1,11):
        print(num,'x',i,'=',num*i)

    #return ("done")
    return


#function ends
        
        

another = "Y"
while (another == "Y"):

    #print (print_multiplication_table())
    print_multiplication_table()
        
    another = input("How about another number?")


print("Thank you")
      
