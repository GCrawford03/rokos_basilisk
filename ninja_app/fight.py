import random

#request.session['stamina'] is a bit of a placeholder, not sure how we're handling stamina at the moment.

def war(request):
    if request.session['stamina'] > 30:
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
        request.session['stamina'] -= 30
    else:
        print('You do not have enough stamina for that!')