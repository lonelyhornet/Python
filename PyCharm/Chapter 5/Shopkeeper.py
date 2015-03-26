import random

money = 100
#money amount
shopname = "name"

shopinv = ["shield", "sword", "healing potion", "armour", "ring", "animal pelt"]
inventory = ["hatchet", "hat"]

c1 = "I see you have a sharp shortsword. Use it well."  #sword
c2 = "You will live to fight another day."  #healing pot
c3 = "Well equipped, are you?"  #shield
c4 = "I see you have a ring, eh? Be careful with it!"  #ring
c5 = "Poor animal you skinned."  #animal pelt
c6 = "That old, rusty hatchet wont be much use."
choice_texts = [c1, c2, c3, c4, c5, c6]
c_choices = [c6]

p_shield = 15
p_sword = 20
p_healing_potion = 50
p_armour = 30
p_ring = 20
p_animal_pelt = 10

print("Would you like to enter the shop? Yes / No ")
enter = input().lower()

while enter == "yes":
    print("\nWhat would you like to do? \n\tA. Leave Shop \n\tB. Buy an item \n\tC. Talk "
          "\n\tD. View items in inventory\n")
    choice = input().lower()

    if choice == "a":
        enter = None

    if choice == "b":
        print("What would you like to buy? Enter the word in '', without the ''.")
        bought = int(input("\n 'Shield': cost: 15"
                        "\n 'Sword': cost: 20"
                        "\n 'Healing Potion': cost: 50"
                        "\n 'Armour': cost: 30"
                        "\n 'Ring': cost: 20"
                        "\n 'Animal Pelt': cost: 10"
                        "\n "))

        if bought == "shield":  #shield
            if money >= p_shield:
                inventory += [shopinv[0]]
                money -= p_shield
                print("You bought: ", [shopinv[0]])
            else:
                print("You do not have enough money, you need", p_shield - money)

        if bought == "sword":  #sword
            if money >= p_sword:
                inventory += [shopinv[1]]
                money -= p_sword
                print("You bought:", [shopinv[1]])
            else:
                print("You do not have enough money, you need", p_sword - money)

        if bought == "healing potion" or "potion":  #healing potion
            if money >= p_healing_potion:
                inventory += [shopinv[2]]
                money -= p_healing_potion
                print("You bought", [shopinv[2]])
            else:
                print("You do not have enough money, you need", p_healing_potion - money)

        if bought == "armour" or "armor": #armour
            if money >= p_armour:
                inventory += [shopinv[3]]
                money -= p_armour
                print("You bought", [shopinv[3]])
            else:
                print("You do not have enough money, you need", p_armour - money)

        if bought == "ring": #ring
            if money >= p_ring:
                inventory += [shopinv[4]]
                money -= p_ring
                print("You bought", [shopinv[4]])
            else:
                print("You do not have enough money, you need", p_ring - money)

        if bought == "animal pelt" or "pelt": #animal pelt
            if money >= p_animal_pelt:
                inventory += [shopinv[5]]
                money -= p_animal_pelt
                print("You bought", [shopinv[5]])
            else:
                print("You do not have enough money, you need", p_animal_pelt - money)

    if choice == "c":
        if "sword" in inventory:
            c_choices += [c3]
            if inventory.count("sword") > 1:
                c_choices.remove(c3)

        if "healing potion" in inventory:
            c_choices += [c2]
            if inventory.count("healing potion") > 1:
                c_choices.remove(c2)

        if "shield" in inventory:
            c_choices += [c3]
            if inventory.count("shield") > 1:
                c_choices.remove(c3)

        if "ring" in inventory:
            c_choices += [c4]
            if inventory.count("ring") > 1:
                c_choices.remove(c4)

        if "animal pelt" in inventory:
            c_choices += [c5]
            if inventory.count("animal pelt") > 1:
                c_choices.remove(c5)

        rand = (random.choice(c_choices))
        print(rand)
        if rand == random.choice(c_choices):
            random.choice(c_choices) #if the roll was the same as the previous, re-roll.


    if choice == "d":
        print("Inventory:", inventory)
        print("Money: ", money)

else:
    print("Okay, come back soon!")
