import random
import operator
import time

pname=input('Choose your player name \n')

calcs = ['+','-','+,-','+,*,/'] # What calculations the player will need to do per level, each list item is a level
rang = ['0,10','0,10','0,10','0,10','0,10'] # What is the range of numbers per level, each list item is a level
ncalc= [1,1,2,1] # Number of calculations per level, each list item is a level
levell = [0,1,3] # Number of levels
atemp = 3 #How many times the player needs to give a right answer (consecutive)
scount = 0 #Counts the consecutive right answers. Every time the player gives a wrong answer it goes back to 0
i = 0 #Used as a counter for the level
n=0 #Used as a counter for the number of calculations
erw=list() #This is a list which concatenates all the random numbers and operators that are generated from the programme in order to print them as a string to the player (the question)
right=0 #Counts how many correct answers the player has given
wrong=0 #Counts how many wrong answers the player has given
ops = {"+": operator.add,"-": operator.sub,"*": operator.mul,"/": operator.truediv} # This allows you later to call the operators and randomly select them

#Below def returns rundom numbers for the range of that level
def no():
    rng=rang[i]
    com = rng.find(',')
    rs= int(rng[:com])
    rf=int(rng[com+1:])
    return (int(random.randint(rs,rf)))

#Below def opsfunc utilises the operator library and randomly picks an operator which is later translated to the actual function
def opsfunc():
    clc=calcs[i]
    if ',' in clc:
        clcs = clc.split(',')
        si = random.choice(clcs)
        return(si)
    else:
        return(clc)

for i in levell:
    print('Welcome to level',i+1,' Answer ', atemp, ' consecutive questions correct and you will pass to the next level \n')
    if i == 0:
        sttime=time.time() #Timer starts
    scount = 0
    erw=list()

    while scount < atemp:

        print('You have answered ', scount, 'correct \n')
        numcalc = ncalc[i]
        n=0
        erw=list()

        while n < numcalc:
            if n == 0:
                no1=no()
                no2=no()
                pros=opsfunc()
                proc = ops[pros]
                erw.append(no1)
                erw.append(pros)
                prax=proc(no1,no2)
                erw.append(no2)
                n=n+1
            elif n>0:
                no3=no()
                pros=opsfunc()
                proc = ops[pros]
                erw.append(pros)
                prax=proc(prax,no3)
                erw.append(no3)
                n=n+1

        print(*erw, sep=' ')
        print('')
        result=input('Write your answer here \n')
        result=float(result)
        prax=float(prax)

        if result == prax:
            scount=scount+1
            print('CORRECT \n')
            right=right+1
        elif result == 'stop':
            break
        else:
            print('Try again \n')
            wrong=wrong+1
            scount=0

fitime=time.time() #Timer finishes
ttime=int(fitime-sttime) #Time required to complete the game

message=('CONGRATULATIONS',pname,'You have answered:',right,'Right. ',wrong,'Wrong ','You have reached level',i+1,'You finished in',ttime, 'sec' ,'It took you', (wrong+right)/ttime, 'sec per question' )
print(*message, sep=' ')
message=str(message)
filename = 'results/' + pname +'results.txt' # Optional code to save the results per game in a txt file. Create the txt file in advance of running the code
file=open(filename,'w')
file.write(message)
