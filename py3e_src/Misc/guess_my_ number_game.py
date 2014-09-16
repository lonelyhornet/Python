# Guess My Number
#

import random  

print("\tWelcome to 'Guess My Number Game'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

# set the initial values
the_number = random.randint(1, 100)
guess = int(input("Please take a guess: "))
tries = 1

# guessing loop
while guess != the_number:
    if guess > the_number:
        print("Try a Lower Number...")
    else:
        print("Try a Higher Number...")
            
    guess = int(input("Take a guess: "))
    tries += 1
    
    if tries > 10:
        print('You lose!')
        input("\n\nPress the enter key to exit.")

print("Correct!  Well done, the number was", the_number)
print("And it only took you", tries, "tries!\n")
  
input("\n\nPress the enter key to exit.")
