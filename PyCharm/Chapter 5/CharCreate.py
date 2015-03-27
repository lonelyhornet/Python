points = 5
HEALTH, STAMINA, ALIGNMENT, AGILITY, STRENGTH, DEXTERITY = 0, 0, 0, 0, 0, 0
attr_num = [HEALTH, STAMINA, ALIGNMENT, AGILITY, STRENGTH, DEXTERITY]
attr_string = ['HEALTH', "STAMINA", "ALIGNMENT", "AGILITY", "STRENGTH", "DEXTERITY"]


while True:
    print('\nWhat would you like to do? \na. Spend points on attributes. \nb. See attribute amounts'
          '\nc. Take points from an attribute back into the pool.\n')
    CHOICE = input().upper()

    if CHOICE == "A":
        print('What attribute would you like to invest in?: ')
        CHOSEN = input().upper()

        if CHOSEN == attr_string[0]: #health
            attr_num[0] += 1
            points -= 1
            print('HEALTH: ', attr_num[0])

        if CHOSEN == attr_string[1]: #stamina
            attr_num[1] += 1
            points -= 1
            print('STAMINA: ', attr_num[1])

        if CHOSEN == attr_string[2]: #alignment
            attr_num[2] += 1
            points -= 1
            print("ALIGNMENT: ", attr_num[2])

        if CHOSEN == attr_string[3]: #agility
            attr_num[3] += 1
            points -= 1
            print("AGILITY: ", attr_num[3])

        if CHOSEN == attr_string[4]: #strength
            attr_num[4] += 1
            points -= 1
            print("STRENGTH: ", attr_num[4])

        if CHOSEN == attr_string[5]: #dexterity
            attr_num[5] += 1
            points -= 1
            print("DEXTERITY: ", attr_num[5])



    if CHOICE == "B":
        print("Current Attributes / Points:"
              "\nPOINTS: ", points,
              "\nHEALTH: ", attr_num[0],
              "\nSTAMINA: ", attr_num[1],
              "\nALIGNMENT: ", attr_num[2],
              "\nAGILITY: ", attr_num[3],
              "\nSTRENGTH: ", attr_num[4],
              "\nDEXTERITY: ", attr_num[5],)


    if CHOICE == "C":
        print("What attribute do you want to take points out of?: ")
        ATTR_REM = input().upper()

        if ATTR_REM == attr_string[0] and attr_num[0] > 0: #health
            attr_num[0] -= 1
            points += 1
            print("HEALTH: ", attr_num[0])

        if ATTR_REM == attr_string[1] and attr_num[1] > 0: #stamina
            attr_num[1] -= 1
            points += 1
            print("STAMINA: ", attr_num[1])

        if ATTR_REM == attr_string[2] and attr_num[2] > 0: #alignment
            attr_num[2] -= 1
            points += 1
            print("ALIGNMENT: ", attr_num[2])

        if ATTR_REM == attr_string[3] and attr_num[3] > 0: #agility
            attr_num[3] -= 1
            points += 1
            print("AGILITY: ", attr_num[3])

        if ATTR_REM == attr_string[4] and attr_num[4] > 0: #strength
            attr_num[4] -= 1
            points += 1
            print("STRENGTH: ", attr_num[4])

        if ATTR_REM == attr_string[5] and attr_num[5] > 0: #dexterity
            attr_num[5] -= 1
            points += 1
            print("DEXTERITY: ", attr_num[5])

        else:
            print("\nThat attribute has no points invested in it yet.")


    if points == 0:
        print("You have no more points left.")
