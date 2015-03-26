#High scores
#Demonstrates list methods

scores = []
choice = None

while choice!= "0":
    print(
        """
        High Scores
        0 - Exit
        1 - Show Scores
        2 - Add a Score
        3 - Delete a Score
        4 - Sort Scores
        """
        )

    choice = input("Choice: ")
    print()

    #exit
    if choice == "0":å
        print("Good-bye.")

    #list high-score table
    elif choice == "1":
        print("High Scores")
        for score in scores:
            print(score)

    elif choice == "2":
        score = int(input("What score did you get?: "))
        scores.append(score)

    #remove a score
    elif choice == "3":
        score = int(input("Remove which score?: "))
        if score in scores:
            scores.remove(score)
        else:
            print(score, "isn't in the high scores list.")

    #sort scores
    elif choice == "4":
        scores.sort(reverse = True) #.sort() sorts in ascending, reverse makes it descending

    #unknown choice
    else:
        print("Sorry, but", choice, "isn't a valid choice.")
