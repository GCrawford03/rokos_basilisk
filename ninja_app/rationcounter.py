#not sure how to get this to display with an auto increment I think we're going to need to use JS or jQuery or ajax, cause right now it still reloads the page and is dependent on a button press to call the funciton. this might be something we all need to tackle together. 

def get_food(request):
    if 'rations' in request.POST:
        if request.session['rations'] < 100:
            request.session['rations'] += 5
        return redirect('/game')