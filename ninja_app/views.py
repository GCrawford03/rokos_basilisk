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

def index(request):
    if "rations" and "stamina" and "prompt" not in request.session:
        request.session['rations'] = 0
        request.session['stamina'] = 0
        request.session['prompt'] = "Would you like to go on an adventure? Type 'yes' or 'no' to begin..."
    return render(request, "index.html")

def game(request):
    if request.method == 'POST':
        yes_no = ["yes", "no"]
        directions = ["west", "east"]
        name = request.session['player_name']
        response = request.POST['input']
        if response not in directions:
            if response == "yes":
                request.session['prompt'] = "You reach a crossroads, would you like to go west and head to battle?(requires 30 Stamina) or east?.\n"
            elif response == "no":
                request.session['prompt'] = "You are not ready for this quest. Goodbye, " + name + ". Please Reset Game"
            else: 
                request.session['prompt'] = "I didn't understand that.\n Please type 'yes' or 'no' to continue"
            return redirect('/game')
        if response not in yes_no:
            if response == "west":
                if request.session['stamina'] >= 30:
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
                        if win > 5:
                            request.session['prompt'] = "You Won!"
                        else: 
                            request.session['prompt'] = "You Lost the Battle! Please Reset Game!"
                    fight()
                else:
                    request.session['prompt'] = "You don't have the stamina for that!"
                return redirect ('/game')
            if response == "east":
                request.session['prompt'] = 'you died'    
            return redirect('/game')

def reset(request):
    request.session['prompt'] = "Would you like to go on an adventure? Type 'yes' or 'no' to begin..."
    return redirect('/game')
