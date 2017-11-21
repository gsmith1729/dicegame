import random
wins=0
losses=0
repeats=1e6
for i in range(0,repeats):
    attempts=0
    x=0
    while x<5/6:
        x=random.random()
        attempts+=1
    if attempts%2==1:
        wins+=1
    else:
        losses+=1
    

outcome=wins/(wins+losses)
