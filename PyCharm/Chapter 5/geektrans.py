#__author__ = 'Lonelyhornet'

dictionary = {"404": "clueless. From the web error message 404, meaning page not found.",
              "Googling": "searching the Internet for background information on a person and/or thing.",
              "Keyboard Plaque": "the collection of debris found in computer keyboards",
              "Link Rot": "the process by which web page links become obsolete.",
              "Percussive Maintenace": "the act of striking an electronic device to make it work.",
              "Uninstalled": "being fired, especially popular during the dot-bomb era."
              }
#creates dictionary called dictionary, consists of 6 pairs called items. Each consist of a key and a value.
#Can use dictionary.get("Potato", "I don't know.") to test for 'Potato' in 'dictionary'.


choice = None
while choice != "0":

    print(
        """

        Word Translator

        0 - Quit
        1 - Look up a term
        2 - Add a term
        3 - Redefine a term
        4 - Delete a term
        """
    )

    choice = input("Choice: ")
    print() #prints what the input was.

    #exit
    if choice == "0":
        print("Good-Bye.")

    #get a definition
    elif choice == "1":
        term = input("What term do you want me to translate?: ")
        if term in dictionary:
            definition = dictionary[term]
            print("\n", term, "means", definition)
        else:
            print("\nSorry I don't know what ", term, "is.")

    #add a term-definition pair
    elif choice == "2":
        term = input("What term do you want me to add?: ")
        if term not in dictionary:
            definition = input("\nWhat's the definition?: ")
            dictionary[term] = definition
            print("\n", term, "has been added.")
        else:
            print("\nThat term already exists. Try redefining it.")
