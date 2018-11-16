def play():


 from random import randint
 player = input('Rock: (r), Paper: (p), Scissors:(s)?')
 cw=0
 pw=0

 if  player == 'r':
    player = 'Rock'
 elif player== 'p':
    player = 'Paper'
 elif player== 's':
    player = 'Scissor'

 print('Player VS. COMPUTER')
 print('  '+ player, 'VS.', end= ' ')

 chosen = randint(1,3) #random number generation used
                      #for random computer's choice.
 if   (chosen==1):
    computer = 'Rock'
 elif (chosen==2):
    computer = 'Paper'
 elif (chosen==3):
    computer = 'Scissor'

 print (computer)

 #RESULTS:

 if player==computer:
    print ('       DRAW')
 elif (player == 'Rock'    and computer =='Scissor'):
    print ('PLAYER WINS THE ROUND')
    pw = pw + 1
 elif (player == 'Rock'    and computer =='Paper'):
    print ('COMPUTER WINS THE ROUND')
    cw = cw + 1
 elif (player == 'Scissor' and computer =='Rock'):
    print ('COMPUTER WINS THE ROUND')
    cw = cw + 1
 elif (player == 'Scissor' and computer =='Paper'):
    print ('PLAYER WINS THE ROUND')
    pw = pw + 1
 elif (player == 'Paper'   and computer =='Rock'):
    print ('PLAYER WINS THE ROUND')
    pw = pw + 1
 elif (player == 'Paper'   and computer =='Scissor'):
    print ('COMPUTER WINS THE ROUND')
    cw = cw + 1
 print('         ')
 return (cw,pw)       #returns scores after each round





game = eval(input('Number of rounds to be played: '))
cp = 0
pp = 0
for i in range(1,game+1):
    print ( '     Round: ' + str(i)+ '\n   ')
    (cw,pw)=play()
    cp = cp + cw              #totals computer's points
    pp = pp + pw              #totals player's points

print ('  Game Scorecard: \n  ')

if (cp>pp):
 print( 'COMPUTER WINS THE GAME BY '+ str(cp)+'-'+str(pp))
elif(pp>cp):
 print( 'PLAYER WINS THE GAME BY '+ str(pp)+'-'+str(cp))
else:
    print ( 'THE GAME RESULTED TO DRAW ')


print('       \nThank you for playing! \n   See you soon ')

