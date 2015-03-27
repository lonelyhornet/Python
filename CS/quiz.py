#Jane Smith
#Task 2: Creating a quiz  - Level 1 of the Online Safety game

import random

players = ["Starplayer", "Ben", "Kev", "Cris", "Runner", "Heart", "Kitty", "Jade", "Moon", "Gem", "Mo", "Ant", "Sword", "Crazy-horse", "Ellie", "Fish"]
#List of registered players

quizQuestions = [["What is CEOP?", "I/Criminal Exploration and Online Protection", "C/Child Exploitation and Online Protection", "I/Child Exploitation and Organised Protectors"],
        ["When you get an email from someone you do not know what should you do?", "C/Delete it and mark as spam.", "I/Reply and say hello.", "I/Forward to your friends."],
        ["How secret should you keep your passwords?", "C/Never give out passwords except to your parents.", "I/Give them only to your best friends.", "I/Give them to strangers."],
        ["When an online contact who frightens you asks to meet you in person what should you do?", "I/Arrange to meet them.", "I/Arrange to meet them with your best friend.", "C/Report to CEOP."],
        ["If an email asks you to enter your bank account details because of a problem with your account what should you do?", "I/Reply to the email.", "I/Enter your bank account details.", "C/Contact the bank to check if they sent the email."]]
#List of questions and answers - correct answers start with C/; incorrect answers with I/

numberOfQuestions = len(quizQuestions)
pointsPerQuestion = 4
#Using variables to store length of quiz and points per question allows the number of questions in the quiz and the number of points per question to be altered easily

level = 1
#Declares a variable for the level

def new_player():
    #Checks that a valid player name is entered
    global playerName
    validName = False
    while validName == False:
        playerName = input ("\nPlease enter your player name: ")
        for name in players:
             if playerName == name:
                 validName = True
        if validName == False:
            print("This name is not registered. Try again.")
 
        else:
            print("Hello",playerName,"- good luck in the quiz!\n")
            print("Rules of the game")
            print("-" * 40)
            print("You will be asked a series of questions about online safety.\nSelect the correct answer by typing in the number when prompted.\nEach correct answer will be awarded 4 points.\nGood luck!\n")
            
def quiz():
        questionsAsked = []
        #Storing the question numbers already asked in a list ensures that each question only appears once

        global score
        score = 0
        questionNumber = random.randint(0, numberOfQuestions - 1)
        while len(questionsAsked) < numberOfQuestions:
            while questionNumber in questionsAsked:
                questionNumber = random.randint(0, numberOfQuestions - 1)
                #Checks if question number has already been selected and chooses another one if needs be
            questionsAsked.append(questionNumber)
            
            question = quizQuestions[questionNumber]
            correctAnswer = ""
            print("")
            print(question[0])
            print("")
            #Prints the question followed by the three possible answers
            for i in range (1, 4):
                if question[i][0] == "C":
                #Identifies correct answer     
                    correctAnswer = i
                print(i, question[i][2:])
            print("")

            chosenAnswer = ""
            while chosenAnswer != "1" and chosenAnswer != "2" and chosenAnswer != "3":
                       chosenAnswer = input ("Please enter 1, 2 or 3: ")
            chosenAnswer = int(chosenAnswer)
            print("")
            if chosenAnswer == correctAnswer:
                print("Is the correct answer.")
                score += 4
            else:
                print("Is incorrect. The correct answer is:", question[correctAnswer][2:])

def result():
    print("-" * 40)
    print("")
    print("That's the end of the quiz.\n")
    print(playerName, "- In level", level, "you scored", score, "out of a possible", numberOfQuestions * pointsPerQuestion, "points.\n")
     
##Main program
print("")
print("Welcome to the Online Safety quiz.")
print("-" * 40)
new_player()
anotherGo = "Y"
while anotherGo == "Y" or anotherGo == "y":
    quiz()
    result()
    anotherGo = input("Another go (Y/N)? ")
print("Thanks for playing. Goodbye!")

    
    
