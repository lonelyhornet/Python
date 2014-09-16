import random

print('I sense your energy. Your true emotions are coming across my screen.')
print('You are...')

mood = random.randint(1, 4)

if mood == 1:
    #Can print image
    print(':D Happy!')

elif mood == 2:
    print(':| Neutral')

elif mood == 3:
    print(':( Sad')
    print('today')

elif mood == 4:
    print('GLaDOS is unable to read your expression. ERROR!!11!')
#PORTAL REFERENCE
input('\n\nPress enter key to exit')
#Imports random (random.randint[eger])
#If mood is 1 print that
#elseif (elif) mood is 2, print neutral
#elif mood is 3 print sad
