print("Welcome to smoothie-matic 2.0")

def make_smoothie():
    
    juice = input ("What juice would you like?")
    fruit = input ("OK, and how about fruit?")

    print("Thanks. Lets go!")
    print("Crushing the ice..")
    print("Blending the " + fruit)
    print("Now  adding in the " + juice + " juice")
    print("Finished! There's your " + fruit + " and " + juice + " smoothie!")

another = "Y"
while (another == "Y" or another == "y" or another == "0719"):

   make_smoothie()
   another = input("How about another(Y/N)?")
    

print("Bye")
      
