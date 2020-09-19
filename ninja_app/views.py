from django.shortcuts import render, redirect
import random, time, sys, random, threading

# test 5

def index(request):
    if "gold" not in request.session:
        request.session['prompt'] = "Would you like to go on an adventure? 'yes/no'"
        request.session['gold'] = 0
    return render(request, "index.html")

def process(request):
    print(request.POST)
    if 'house' in request.POST:
        request.session['gold'] += int(random.random() * 2 + 7)
    if 'casino' in request.POST:
        if int(random.random() * 10) > 5:
            request.session['gold'] += int(random.random()*50)
        else:
            request.session['gold'] -= int(random.random()*50)
    if 'farm' in request.POST:
        request.session['gold'] += int(random.random() * 5 + 15)
    if 'cave' in request.POST:
        request.session['gold'] += int(random.random()* 10 + 30)
    print(request.session['gold'])
    return redirect('/')


# def counter():
#     cps = 0
#     speed = 0.01

#     while True:
#         """Prints the amount of Clicks per Second and resets the counter every second."""

#         global cps
#         print("Clicks Per Second {}  ".format(cps), end = "\r"
#         cps = 0
#         time.sleep(1)

def countdown(request):
    while request > 0:
        sys.stdout.write('\rDuration : {}s'.format(request))
        request -= 1
        sys.stdout.flush()
        time.sleep(1)

# def randomdig(request):
#     x = "treasure chest", "sack of gold"

# print(random.choice(x))


# text adventure input/output
def game(request):
    if request.POST['input']== "yes":
        request.session['prompt']= "You reach a crossroads. Would you like to go 'west' or 'east'?"
        if request.POST['input']== "no":
            request.session['prompt']= "You died."
    if request.POST['input']== "west":
        request.session['prompt']= "You encounter a monster. Would you like to 'run' or 'attack'?"
    if request.POST['input']== "east":
        request.session['prompt']= "You get lost. 'ok'"
    if request.POST['input']== "attack":
        request.session['prompt']= "You died."
    if request.POST['input']== "run":
        request.session['prompt']= "You run away and find food ('continue')"
        request.session['gold'] += int(random.random() * 50 + 200)
    if request.POST['input']== "continue":
        request.session['prompt']= "placeholder text."

    print(request.POST)
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')

    # weapons/etc

class Item():
    # the base class for all items/drones
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

class Robot(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class DroneOne(Robot):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value, damage)
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class WayneBot(Robot):
    def __init__(self):
        super().__init__(name="Stick",
                         description="That's a big stick.",
                         value=0,
                         damage=5)
 
class DroneThree(Robot):
    def __init__(self):
        super().__init__(name="Drone Three",
                         description="Add a description.",
                         value=10,
                         damage=10)                
                        
class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
 
    def is_alive(self):
        return self.hp > 0

class Raider(Enemy):
    def __init__(self):
        super().__init__(name="Add a description.", hp=10, damage=2)



# text adventure in terminal

# answer = input ("Would you like to play? (yes/no) ")
# if answer.lower().strip() == "yes":
#     answer = input("You reach a crossroads. Would you like to go 'left' or 'right'?").lower().strip()
#     if answer == "left":
#         answer = input("You encounter a monster. Would you like to 'run' or 'attack'?")
        
#         if answer == "attack":
#             print("The monster deals 100 damage and kills you.")
#         else:
#             print("Good choice, you made it away safely.")

#     elif answer == "right":
#         print("You notice a small village in the distance. Do you 'go towards it' or 'continue on your path'?")

#         if answer == "go towards it":
#             print("A merchant wearing a cloak approaches you and asks if you want to see their wares. 'yes/no'")

#             if answer == "yes":
#                 print("You see a sword. Do you 'purchase' it or 'steal' it?")

#         else:
#             print("That's too bad. They might've had something you wanted for sale.")