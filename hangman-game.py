word = input('Which word would you like player 2 to guess? \n') #Provide the word that the other player would like to guess

# The code below will enter 30 blank lines so the input from the player above won't be seen from the player guessing
elin = 0
while elin < 30:
    print('\n')
    elin = elin +1
   
chan = input('How many chances do you want to give the player? \n') # Input how many chances are given to the oponent to guess the word

word = str(word)
wlen = len(word)
wlen = int(wlen)
fl = word[0]
ll = word[wlen-1]
z = 0

# This will print the guessing word with the first and last letter showing but with any letters in between showing as _
for i in word:
    z = z + 1
    if z == 1:
        print (i, end =' ')
    elif z == wlen:
        print (i, end =' ')
    else:
        print ('_', end =' ')

malo = 1
chan = int(chan)
tabl =[]

# This is the loop where player is guessing letter by letter
while malo > 0:

    print ('\nYou have ', chan, ' left \n')
    guess = input('Guess the letter \n')

    guess =str(guess)
    cl= -1
    cl=int(cl)

    if guess in word:
        print('Found one!!!')

        for i in word:
            cl = cl+1
            if guess == i:
                break

        laslet = [cl]

        dac = 0
        dac = int(dac)
        z = 0

        for i in word:
            z = z + 1
            if z == 1:
                print (i, end =' ')
            elif z == wlen:
                print (i, end =' ')
            elif i in tabl:
                print (i, end =' ')
            elif i == word[cl]:
                tabl.append(i)
                print (i, end =' ')
            else:
                print ('_', end =' ')
                dac = dac + 1

        if dac == 0:

            print('\nYOU WON')
            break

    else:
        chan = chan - 1
    if chan == 0:

        print ('\nYOU LOST')
        print('The word is ',word)
        break
