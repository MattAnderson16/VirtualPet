#Virtual Pet

class VirtualPet:
    #docstring
    """An implementation of a virtual pet"""
    #constructor method - runs automatically
    def __init__(self,name):
        self.name = name
        self.hunger = 50
        print("Hi! I have been born and my name is {0}".format(name))
    #method
    def talk(self):
        if self.hunger > 70:
            print("I am hungry! please feed me!")
        else:
            print("You try talking to {0} but all you hear is a series of wierd sounds".format(name))

    def eat(self,food):
        if food == "bread":
            hunger -=20
        if food == "cake":
            hunger -=15
        if food == "chocolate":
            hunger -=10
        print("that {0} was yummy!".format(food))

def displaymenu(name):
    print()
    print("Main Menu")
    print()
    print("1. Feed {0}".format(name))
    print("2. Talk to {0}".format(name))
    print("3. Take {0} for a walk".format(name))
    print("9. Quit")
    print()

def getmenuchoice():
    choice = input("What would you like to do >>> ").lower()
    while choice not in ["1","2","3","9"]:
        print()
        print("Please enter a valid choice")
        print()
        choice = input("What would you like to do >>> ").lower()
    print()
    return choice

def displayfood(chocolate,cake,bread):
    print()
    print("Available food:")
    print()
    print("Chocolate >>> {0}".format(chocolate))
    print("Cake >>> {0}".format(cake))
    print("Bread >>> {0}".format(bread))
    print()

def getfood(chocolate,cake,bread,name,pet_one):
    food = input("Please choose one of the available foods to feed to {0}".format(name)).lower()
    print()
    valid = False
    while not valid:
        if food == "":
            yn = input("Are you sure you don't want to feed {0} >>> ".format(name)).lower()
            yn = yn[0]
            print()
            if yn == "y":
                if pet_one.hunger == 100:
                    print("{0} has starved to death, I hope you're happy!".format(name))
                    valid = True
                else:
                    pet_one.hunger +=10
                    if pet_one.hunger == 100:
                        print("{0} has starved to death, I hope you're happy!".format(name))
                        valid = True
                    else:
                        valid = True
        elif food not in ["chocolate","cake","bread"] and (chocolate != 0 and  cake != 0 and bread!= 0):
            print("Please choose one of the available foods")
            food = input("Please choose one of the available foods to feed to {0}".format(name)).lower()
        elif food == "chocolate" and chocolate == 0:
            print("you are out of chocolate, please choose some other food")
            food = input("Please choose one of the available foods to feed to {0}".format(name)).lower()
        elif food == "cake" and cake == 0:
            print("you are out of cake, please choose some other food")
            food = input("Please choose one of the available foods to feed to {0}".format(name)).lower()
        elif food == "bread" and bread == 0:
            print("you are out of bread, please choose some other food")
            food = input("Please choose one of the available foods to feed to {0}".format(name)).lower()
        elif (chocolate != 0 and  cake != 0 and bread!= 0):
            print("you are out of food!")
            food = ""
            valid = True
        elif food in ["chocolate","cake","bread"]:
            valid = True
            

if __name__ == "__main__":
    chocolate = 5
    cake = 5
    bread = 5
    name = input("Please choose a name for your pet >>> ")
    #instantiation
    pet_one = VirtualPet(name)
    choice = ""
    while choice != "9":
        displaymenu(name)
        choice = getmenuchoice()
        if choice == "1":
            displayfood(chocolate,cake,bread)
            food = getfood(chocolate,cake,bread,name,pet_one)
            if food != "":
                pet_one.eat(food)
            else:
                pet_one.hunger +=10
        elif choice == "2":
            pet_one.talk()
