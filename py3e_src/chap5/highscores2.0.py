#High Scores 2.0
#Demonstrates nested sequences

scores = []
choice = None

while choice != "0":
    print(
    """
    High Scores 2.0

    0 - Quit
    1 - List Scores
    2 - Add a Score
    """
    )

    choice = input("Choice: ")
    print()

    #exit
    if choice == "0":
        print("Good-bye.")

    #display high-score table
    elif choice == "1":
        print("High Scores\n")
        print("NAME\tSCORE")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)


