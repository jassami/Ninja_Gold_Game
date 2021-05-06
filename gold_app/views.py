from django.shortcuts import render, redirect
from time import strftime
from pytz import timezone
from datetime import datetime
import pytz
import random

location = {
    'farm': (10,20),
    'cave': (5,10),
    'house': (2,5),
    'casino': (-50,50)
}
def index(request):
    return render(request, 'index.html')

def process(request):
    request.session['goldnum'] = request.POST['goldnum']
    request.session['movenum'] = request.POST['movenum']
    return redirect('/home')

def home(request): 
    if not 'gold' in request.session:
        request.session['gold'] = 0
        request.session['move'] = 0
        request.session['active'] = []        
    return render(request, 'home.html')

def process_money(request, place):
    dt = datetime.now(timezone("US/Central"))
    now = dt.strftime("%Y/ %m/ %d %I:%M %p")
    request.session['move'] +=1
    earned_gold = random.randint(location[place][0],location[place][1])
    request.session['gold'] += earned_gold
    if int(request.session['gold']) == int(request.session['goldnum']) and int(request.session['move']) <= int(request.session['movenum']):
        request.session['active'].append('You won!')
    elif int(request.session['gold']) > int(request.session['goldnum']) or int(request.session['move']) >= int(request.session['movenum']):
        request.session['active'].append('You lost :(')
    else:
        if earned_gold >0:
            request.session['active'].append(f"Earned {earned_gold} golds from the {place}! {now}")
        else:
            earned_gold = abs(earned_gold)
            request.session['active'].append(f"Entered a casino and lost {earned_gold} golds... Ouch.. {now}")
    return redirect('/home')

def reset(request):
    request.session. clear()
    return redirect('/')
