from django.shortcuts import render, redirect
import random, time, sys, random, threading
from .models import *
from .textgame import *
from django.contrib import messages


def homepage(request):
    return render(request, 'landing.html' )

def register(request):
    if request.method == 'POST':
        errors = User.objects.validate(request.POST)
        print(errors)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        new_user = User.objects.create(
            first_name=request.POST['first_name'])
        request.session['player_name'] = new_user.first_name
        request.session['player_id'] = new_user.id
        return redirect('/game')
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

def get_rations(request):
    if request.method == 'POST':
        if request.session['rations'] < 100:
            request.session['rations'] += 5
    return render(request, 'ration.html')   

def train(request):
    if request.method == 'POST':
        if request.session['rations'] >= 10:
            request.session['rations'] -= 10
            request.session['stamina'] += 1
    return render(request, 'ration.html')

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
    if "rations" and "stamina" and "prompt" not in request.session:
        request.session['rations'] = 0
        request.session['stamina'] = 0
        request.session['prompt'] = "Would you like to go on an adventure? Type 'yes' or 'no' to begin..."
    return render(request, "index.html")

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
    if request.method == "POST":
        if request.POST['input']== "yes":
            request.session['stamina'] -= 1
            request.session['prompt']= "You reach a crossroads. Would you like to go 'west' or 'east'?"
            if request.POST['input']== "no":
                request.session['prompt']= "You died."
                request.session['stamina'] -= 1
        if request.POST['input']== "west":
            request.session['prompt']= "You encounter a monster. Would you like to 'run' or 'attack'?"
            request.session['stamina'] -= 1
        if request.POST['input']== "east":
            request.session['prompt']= "You get lost. 'ok'"
            request.session['stamina'] -= 1
        if request.POST['input']== "ok":
            request.session['prompt']= "You stumble upon something"
            request.session['stamina'] -= 1
        if request.POST['input']== "attack":
            request.session['prompt']= "You died."
            request.session['stamina'] -= 1
        if request.POST['input']== "run":
            request.session['prompt']= "You run away and find food ('continue')"
            request.session['rations'] += int(random.random() * 50 + 200)
            request.session['stamina'] -= 1
        if request.POST['input']== "continue":
            request.session['prompt']= "placeholder text."
            request.session['stamina'] -= 1


    print(request.POST)
    return redirect('/game')

def reset(request):
    request.session['prompt'] = "Would you like to go on an adventure? Type 'yes' or 'no' to begin..."
    return redirect('/game')
