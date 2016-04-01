#Create dog class
#Create constructor and initialize the attributes
#Define functions
#Define give_details function
#call the method
#print details

class Dog:
    def __init__(self, name, breed, weight, size):
        self.name = name
        self.breed = breed
        self.weight = weight
        self.size = size

    def move(self, movement):
        self.move = movement
        
    def eat(self, eating_habit):
        self.eat = eating_habit

    def make_sound(self, sound):
        self.make_sound = sound
        
    def give_details(self):
        details = input(self.move, self.eat, self.make_sound)
        print (details)
 
pet = Dog(Bubb, labrador, 30, 56)

pet.give_details(self)
