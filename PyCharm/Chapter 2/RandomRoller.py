import random
die1 =  random.randint(1,6)
die2 = random.randrange(6) + 1
total = die1 + die2
print('You rolled a ', die1, 'and a ', die2, 'for a total of ', total)
input('\n\nPress the enter key to exit')

#Imports 'random' and sets var die1 & die2 to random.randint (random int)
#And sets die2 to random range between 6 + 1
#Prints die1 & die2 var (sets the randint/range into that var)
