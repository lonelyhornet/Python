inventory = () #Empty inventory tuple

if not inventory: #if inventory has nothing
    print("You are empty handed")

inventory = ("sword",
            "armour",
            "shield",
            "healing potion") #assigns elements to the tuple

print("The tuple inventory is:")
print(inventory)

print("Your items:")
for item in inventory:
    print(item)

index = int(input("enter index: "))
print("at index", index, "is", inventory[index]) #each tuple element is assigned an index number
#indexing starts at 0, so 0 = sword, 1 = armour, 2 = shield. Also works backwards, -1 = healing potion, -2 = shield