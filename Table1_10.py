#WAP to loop through and print the multiplication table of 1-10.

print ("\t \t \t \t Table of 1-10")
#function begins
def print_multiplication_table(num):
    for i in range(1,11):
        print(num,'x',i,'=',num*i)
    return
#function ends
        
for item in range (1,11):
    print ("Multiplication table of %d " % item)
    print_multiplication_table(item)
    print ("___________________________________")

print("Thank you")
      

