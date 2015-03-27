#Jane Smith
#Task 1: Registering a new player

def details():
    #Prompts player to enter their details
    print(" ")
    age = input("Please enter your age: ")
    #Converts single letter entry into whole word/phrase
    gender = input("Are you male or female? Enter M for male or F for Female: ")
    if gender == 'f' or gender == 'F':
        gender = "female"
    elif gender == 'm' or gender == 'M':
        gender == 'male'
    else:
        gender = "not specified"
    email = input("Please enter your email address: ")
    playerName = input("Please choose a player name: ")
    print(" ")
    print("These are the details you have entered:")
    print("\nAge:", age, "\nGender:", gender, "\nEmail address:", email,"\nPlayerName:", playerName)

    #Checks if details entered are correct and - if so - ends program
    correct = input("\nIs this information correct? Enter Y for Yes or N for No: ")
    if correct == "y" or correct == "Y":
        print("Thank you for entering your details. ")
        print("Registration complete.")
    else:
        #If the player enters anything other than 'Y', i.e. 'N', the player is prompted to enter their details again
        details()
        
#Start of main program
print("Welcome to the Online Safety game.")
print("-" * 42)
print("To register for the Online Safety game, please answer these questions:")
    
#This will run the function 'details'
details()


