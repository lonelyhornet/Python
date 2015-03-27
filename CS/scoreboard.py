#Jane Smith
#Task 3: Creating a scoreboard

#Reads from the text file "playerScores.txt"
file = open("playerScores.txt", "r")
playerScores = file.readlines()
file.close()
length = len(playerScores)

#Splits each line of playerScores into a list of strings
errorLog = open("scoreboard_error_log.txt", "w")
index = 0
playerData = []

for line in playerScores:
        player, level, score = line.split(",")
        
        #Checks for invalid records and writes any found to error log
        if int(level) < 1 or int(level) > 5 or int(score) <0 or int(score)>20:
                errorLog.write(player)
                errorLog.write(",")
                errorLog.write(level)
                errorLog.write(",")
                errorLog.write(score)
        else:
        #Appends valid score data to a list called playerData
             playerData.append(playerScores[index].split(","))
        index += 1
errorLog.close()

#Sorts the playerData list into alphabetical order of player name
playerData.sort()
numberOfItems = len(playerData)

#Row titles for table used in Options A and B
levelList = ["Level 1", "Level 2", "Level 3", "Level 4", "Level 5"]

def option_A():
#Prints scores for a selected player
        selectedPlayer = input("Enter player name: ")
        found = False
        #Sets the default score for each level to zero
        level1Score = 0
        level2Score = 0
        level3Score = 0
        level4Score = 0
        level5Score = 0
 
        #Finds the selected player's scores and assigns them to the appropriate variables, depending on the level
        for i in range (numberOfItems):
                nextRecord = playerData[i]
                level = int(nextRecord[1])
                score = int(nextRecord[2])
                if nextRecord[0] == selectedPlayer:
                        found = True
                        if level == 1:
                                level1Score = score
                        elif level == 2:
                                level2Score = score
                        elif level == 3:
                                level3Score = score
                        elif level == 4:
                                level4Score = score
                        elif level == 5:
                                level5Score = score

        #Deals with input of an invalid player name
        if found == False:
                print("Invalid player name")
                option_A()
        else:
        #Displays the scores for the selected player in a table
                print ("\nThe level scores for" , selectedPlayer , "are:\n")
                print ("Game level\tScore")
                print ("_" * 21,"\n")
                print (levelList[0],"\t\t", level1Score)
                print (levelList[1],"\t\t", level2Score)
                print (levelList[2],"\t\t", level3Score)
                print (levelList[3],"\t\t", level4Score)
                print (levelList[4],"\t\t", level5Score,"\n")

        return_to_menu()
    
def option_B():
#Displays player with the highest score at each level
        level1HighestScore = 0
        level2HighestScore = 0
        level3HighestScore = 0
        level4HighestScore = 0
        level5HighestScore = 0

        #Creates a set of lists to hold the names of the players who achieve the highest score at each level
        level1TopScorers = []
        level2TopScorers = []
        level3TopScorers = []
        level4TopScorers = []
        level5TopScorers = []

        for i in range (numberOfItems):
            nextRecord = playerData[i]
            player = nextRecord[0]
            level = int(nextRecord[1])
            score = int(nextRecord[2])
            
            #Finds the highest score at each level
            if level == 1 and score > level1HighestScore:
                    level1HighestScore = score
            elif level == 2 and score > level2HighestScore:
                    level2HighestScore = score
            elif level == 3 and score > level3HighestScore:
                    level3HighestScore = score
            elif level == 4 and score > level4HighestScore:
                   level4HighestScore = score
            elif level == 5 and score> level5HighestScore:
                   level5HighestScore = score
        
        #Finds players who have achieved the highest score at each level and adds their names to the appropriate TopScorer iist
        for i in range (numberOfItems):
                nextRecord = playerData[i]
                player = nextRecord[0]
                level = int(nextRecord[1])
                score = int(nextRecord[2])
                if level == 1 and score == level1HighestScore:
                       level1TopScorers.append(player)                       
                elif level == 2 and score == level2HighestScore:
                      level2TopScorers.append(player)       
                elif level == 3 and score == level3HighestScore:
                      level3TopScorers.append(player)       
                elif level == 4 and score == level4HighestScore:
                      level4TopScorers.append(player)       
                elif level == 5 and score == level5HighestScore:
                      level5TopScorers.append(player)       

        #Displays the results in a table
        print ("\nThe highest scorers for each level are:\n\nLevel\tHighest Score\tPlayers")
        print ("______________________________________________\n")
        print (levelList[0], "\t", level1HighestScore, "\t\t")
        for item in level1TopScorers:
                print("\t\t\t", item)
        print (levelList[1], "\t", level2HighestScore, "\t\t")
        for item in level2TopScorers:
                print("\t\t\t",item)
        print (levelList[2], "\t", level3HighestScore, "\t\t")
        for item in level3TopScorers:
                print("\t\t\t",item)
        print (levelList[3], "\t", level4HighestScore, "\t\t")
        for item in level4TopScorers:
                print("\t\t\t", item)
        print (levelList[4], "\t", level5HighestScore, "\t\t")
        for item in level5TopScorers:
                print("\t\t\t",item)

        return_to_menu()

def option_C():
#Displays the player(s) with the overall highest score
        highestScore = 0
        totalForEachPlayer = []
        currentTotal = 0
        previousName = ""
 
        for item in playerData:
                currentItem = item
                currentName = item[0]
                currentScore = int(item[2])
                if currentName == previousName:
                       currentTotal += currentScore
                else:
                        totalForEachPlayer.append([previousName, currentTotal])
                        previousName = currentName
                        currentTotal = currentScore
 
                if currentTotal > highestScore:
                        highestScore = currentTotal

        totalForEachPlayer.append([previousName, currentTotal])                      

        print("The highest score in the game was", highestScore, "and was achieved by: ")
        for item in totalForEachPlayer:
                if item[1] == highestScore:
                        print(item[0])

        return_to_menu()
  
def return_to_menu():
#Prompts to return to menu after options A, B or C have been selected
        backToMenu = False
        print("")
        while backToMenu == False:
                choice = input("Enter Y to return to menu. ")
                if choice == "Y" or choice =="y":
                        backToMenu = True          
        menu()
    
def menu():
#Displays the menu and asks the player to enter an option choice
        again = True
        print("\n_________Scoreboard_________\n")
        print("Option A\tScores for a player\nOption B\tHighest scorer for each level\nOption C\tHighest scorer in the game\n\nEnter Q to quit the scoreboard\n")
        optionsChoice = input("Please enter an option (A, B, C or Q): ")
        while again == True:
                if optionsChoice == "a" or optionsChoice == "A":
                        option_A()
                elif optionsChoice == "b" or optionsChoice == "B":
                        option_B()
                elif optionsChoice == "c" or optionsChoice == "C":
                        option_C()
                elif optionsChoice == "q" or optionsChoice == "Q":
                        again = False
                else:
                        menu()
                break
        
def end_program():
         print("Goodbye")
         
###Main program###  
menu()
end_program()




