WAP to print all the odd/ even numbers from 0 to a number input by the user and as per his input (odd or even).

print("Heyya!")

#numbers = range(1,10)
g = int (input ("enter the last number: "))
#input = int(g)
asshole = range(0, g)


even = []
odd = []

for raj in asshole:
   if (raj % 2) == 0:
        even.append(raj)

   elif (raj % 2) == 1:
       
        odd.append(raj)
    

print (even)
print (odd)
