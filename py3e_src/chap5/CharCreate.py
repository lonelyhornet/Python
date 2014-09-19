#__author__ = 'Lonelyhornet'
#Character Creation program
#Player has 5 points to spend on 4 attributes: strength, health, wisdom, dexterity
#able to spend points on attributes, and take points from them.

points = 5

STRENGTH = 0
DEXTERITY = 0
WISDOM = 0
HEALTH = 0
attributes = ["STRENGTH", "DEXTERITY", "WISDOM", "HEALTH"]
attr_list = [STRENGTH, DEXTERITY, WISDOM, HEALTH]

while 1 > 0:
    CHOICE = input("\nWhat would you like to do? \na. Spend points on attributes. \nb. See attribute amounts"
                   "\nc. Take points from an attribute back into the pool.\n" ).upper()

    if CHOICE == "A":
        TEMP_CHOSEN = input("What attribute would you like to invest in?: ").upper()

        if TEMP_CHOSEN == "STRENGTH":
            STRENGTH += 1
            points -= 1

        if TEMP_CHOSEN == "DEXTERITY":
            DEXTERITY += 1
            points -= 1

        if TEMP_CHOSEN == "WISDOM":
            WISDOM += 1
            points -= 1

        if TEMP_CHOSEN == "HEALTH":
            HEALTH += 1
            points -= 1

    if CHOICE == "B":
        print("Current Attributes / Points:"
              "\nPOINTS: ", points,
              "\nSTRENGTH: ", STRENGTH,
              "\nDEXTERITY: ", DEXTERITY,
              "\nWISDOM: ", WISDOM,
              "\nHEALTH: ", HEALTH,
              "")

    if CHOICE == "C":
        ATTR_REM = input("What attribute do you want to take points out of?: ").upper()

        if ATTR_REM == "STRENGTH" and STRENGTH > 0:
            STRENGTH -= 1
            points += 1

        if ATTR_REM == "DEXTERITY" and DEXTERITY > 0:
            DEXTERITY -= 1
            points += 1

        if ATTR_REM == "WISDOM" and WISDOM > 0:
            WISDOM -= 1
            points += 1

        if ATTR_REM == "HEALTH" and HEALTH > 0:
            HEALTH -= 1
            points += 1

        else:
            print("\nThat attribute has no points invested in it yet.")

    if points == 0:
        print("You have no more points left.")
