inventory = ["sword","armour","shield","healing potion"] #Declares array 'inventory' with strings stated
print("Your items: ")
for items in inventory: #declares elements in inventory as 'items'
    print(items) #Prints all items in inventory

print("You have", len(inventory), "items in your possession.") #len states the length of said array

#test the membership with in
if "healing potion" in inventory: #Checks if 'healing potion' is in the inventory array
    print("You will live to fight another day.")
