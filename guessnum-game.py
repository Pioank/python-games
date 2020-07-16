import random
import datetime

pone=input('Give player one name \n') # Asks player's one name
ptwo=input('Give player two name \n') # Asks player's two name

chances=5 # Control the chances that players have to guess the exact number
p1c=chances
p2c=chances
p1a=None #player 1 answer / guess
p2a=None #player 2 answer / guess
c=1 #even - odd players' turns
p1a=None
p2a=None
winner='no-one'
i=0
var=None
closew=''
pt=0

guessnum=int(random.randint(100,1000)) # Set the range where the random number players are trying to guess will be generated

def answerl():
    if num < guessnum:
        print('Guess higher \n')
        var = 0
    elif num > guessnum:
        print('Guess lower \n')
        var = 0
    elif num == guessnum:
        var = 1
    return(var)

while i < 2*chances:

    if (i % 2) == 0:
        print(pone, ' guess a number')
        p1a=input()
        num=int(p1a)
        answer=answerl()
        pt=1
        if answer==1:
            winner=pone
            break
    else:
        print(ptwo, 'P2 guess a number')
        p2a=input()
        num=int(p2a)
        answer=answerl()
        pt=2
        if answer==1:
            winner=ptwo
            break

    if i == 0:
        closest = num - guessnum
        closest = abs(closest)
        closestn = num
        if pt == 1:
            closew=str(pone)
        elif pt==2:
            closew=str(ptwo)
    elif abs(num-guessnum) < closest:
        closest = abs(num-guessnum)
        closestn = num
        if pt == 1:
            closew=str(pone)
        elif pt==2:
            closew=str(ptwo)

    i=i+1

# If no-one guesses the number then declare winner the player who guessed the closest
if winner=='no-one':
    print('The correct answer was', guessnum)
    print('The closest answer was given by', closew, 'Number: ', closestn)
else:
    print('The winner is:',winner)

datetime_object = str(datetime.datetime.now())

# Code below is to store game results and keep history in a txt - optional
with open('resultsguess/results.txt', 'a+') as file:
    file.write(datetime_object)
    file.write('\n')

    if winner=='no-one':
        file.write('Closest guess was from: ')
        file.write(closew)
        file.write('\n')
        file.write('The correct answer was: ')
        file.write(str(guessnum))
    else:
        file.write('The winner is: ')
        file.write(winner)

    file.write('\n')
    file.write('There were 2 players: ')
    file.write(pone)
    file.write(' and ')
    file.write(ptwo)
    file.write('\n')
