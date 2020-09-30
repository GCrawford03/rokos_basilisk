from django.shortcuts import render, redirect
import random, time, sys, random, threading
from .models import *
from .textgame import *
from django.contrib import messages


def homepage(request):
    return render(request, 'homepage.html' )

def register(request):
    if request.method == 'POST':
        errors = Player.objects.reg_val(request.POST)
        print(errors)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        new_player = Player.objects.create(
            username=request.POST['username'],
            password=request.POST['password'])
        request.session['player_name'] = new_player.username
        request.session['player_id'] = new_player.id
        request.session['current_place'] = 'woods' 
        return redirect('/game')
    return redirect('/')

def login(request):
    if request.method == 'POST':
        logged_player = Player.objects.filter(username=request.POST['username'])
        if len(logged_player):
            logged_player = logged_player[0]
            if (request.POST['password'], logged_player.password):
                request.session['player_name'] = logged_player.username
                request.session['player_id'] = logged_player.id
                request.session['current_place'] = 'woods'
                return redirect('/game')
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

<<<<<<< HEAD
def get_food(request):
=======
def get_rations(request):
>>>>>>> 3829d871a64afcc7d51f79889970e5128b0099de
    if request.method == 'POST':
        if request.session['rations'] < 100:
            request.session['rations'] += 5
    return render(request, 'ration.html')   

<<<<<<< HEAD
#def train(request):
#    if request.method == 'POST':
#        while (request.session['stamina'] < 30):
=======
def train(request):
    if request.method == 'POST':
        if request.session['rations'] >= 10:
            request.session['rations'] -= 10
            request.session['stamina'] += 1
    return render(request, 'ration.html')
>>>>>>> 3829d871a64afcc7d51f79889970e5128b0099de


#def train(request, input, id){
 #   stamina_total = 0;
    
#    while (stamina_total < 30 and input = "train"){

 #       request.session['rations_total'] -= 10
 #       request.session['stamina_total'] += 1
        
 #       if (stamina_total == 30) {

  #          request.session['prompt'] = "Placeholder : Time to go to wor! Type in 'wartime' to go to travel to the battlegraounds."  
  #      }
  #      else{
            
  #          request.session['prompt'] = " Placeholder: Keep training to become a mega superpower! Type 'train' to gain  more stamina."
  #      }
  #  }
  #  return redirect('/game/main')
#}    

def war(request):
    if request.session['stamina'] > 30:
        request.session['stamina'] -= 30
        def fight():
            win = 0
            lose = 0
            battle = 0
            battleresult = random.randint(1, 2)
            while True:
                battle += 1

                if battle > 10:
                    break
                if battleresult == 1:
                    win += 1
                elif battleresult == 2:
                    lose += 1
                battleresult = random.randint(1, 2)
            print(win)
            print(lose)
        fight()
    else:
        print('You do not have enough stamina for that!')


# i'm pretty sure I'm only using methods above this



# test 4

def index(request):
    if "rations" and "stamina" not in request.session:
        request.session['prompt'] = "Would you like to go on an adventure? 'yes/no'"
        request.session['rations'] = 0
        request.session['stamina'] = 0
    context={
        'place': locations[request.session['current_place']]
    }
    return render(request, "index.html",context)

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
    return redirect('/game')


# not finished below

#Disregard this
#def get_food(request, username:
    #one_player = Player.objects.get(id=id)
    #if request.method == 'POST':
        #one_player.rations = request.POST['rations']
        #one_player.save()
        #return redirect('/game')

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
# game states. Starts at 0 and only allows certain inputs
# game model, users have game saves (1:1, 1:Many)
# 
def game(request):
    if request.POST['input']== "yes":
        request.session['prompt']= "You reach a crossroads. Would you like to go 'west' or 'east'?"
        if request.POST['input']== "no":
            request.session['prompt']= "You died."
    if request.POST['input']== "west":
        request.session['prompt']= "You encounter a monster. Would you like to 'run' or 'attack'?"
    if request.POST['input']== "east":#
        request.session['prompt']= "You get lost. 'ok'"
    if request.POST['input']== "ok":
        request.session['prompt']= "You stumble upon something"
    if request.POST['input']== "attack":
        request.session['prompt']= "You died."
    if request.POST['input']== "run":
        request.session['prompt']= "You run away and find food ('continue')"
        request.session['gold'] += int(random.random() * 50 + 200)
    if request.POST['input']== "continue":
        request.session['prompt']= "placeholder text."

    print(request.POST)
    return redirect('/game')

def reset(request):
    request.session.flush()
    return redirect('/game')

#remove after testing
def clear(request):
    if request.session['rations'] == 100:
        request.session['rations'] -= 100
    return redirect('/game')



# text adventure

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