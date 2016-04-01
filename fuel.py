print ("welcome")
g = input ("guess the number : ")
guess = int (g)

if guess == 5 :
    print ("you win")
else:
    if guess > 5:
        print ("too high")
    else:
        print ("too low")

print ("game over")
