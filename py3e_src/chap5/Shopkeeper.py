#shopkeeper script
#simple test using len, lists and such.
#__author__ = "lonelyhornet"

shopname = "name"
keys = []
shopinv = ["shield", "sword", "healing potion", "armour", "ring", "animal pelt"]
shopsize = len(shopinv) - 1
inventory = ["hatchet","hat"]
invsize = len(inventory)



enter = input("Would you like to enter the shop? Yes / No ").lower() #converts input string to lower cases

if enter == ("yes"):
    print("\tWelcome to my shop. Here is the key: ")
    keys.append("shop")
    #keys[:0] = ["shop"]
    print("---------------------------------")
    print("You now have 1 key for: " + keys[0])
    print("---------------------------------")

while enter == ("yes"): #main loop
    choice = input("\nWhat would you like to do? \n\tA. Leave Shop \n\tB. Buy an item \n\tC. Talk \n").lower()

    if choice == ("a"):
        enter = None #enter is none, so loop ends

    if choice == ("b"):
        print("What would you like to buy? Enter a number between 0 and " + str(shopsize)) #states the shop size
        bought = int(input("\n 0 = Shield"
                    "\n 1 = Sword"
                    "\n 2 = Healing Potion"
                    "\n 3 = Armour"
                    "\n 4 = Ring"
                    "\n 5 = Animal Pelt"
                    "\n "))
        print("You have bought: " + shopinv[bought])
        inventory += [shopinv[bought]]
        #inventory[:0] = [shopinv[bought]] #old method which put the bought item in front


    if choice == ("c"):
        print("I do not wish to talk right now, please leave me alone.")

#        if "sword" in inventory:
#            print("I see you have a sharp shortsword.å Use it well.")
#
#        if "healing potion" in inventory:
#            print("You will live to fight another day.")
#
#        if "armour" in inventory:
#            print("Well equipped, are you?")
#
#        if "ring" in inventory:
#            print("I see you have a ring, eh? Be careful with it!")
#        if "animal pelt" in inventory:
#            print("Poor animal you skinned.")

else:
    print("Okay, come back soon!")









