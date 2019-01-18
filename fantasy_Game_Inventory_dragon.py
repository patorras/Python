

inv = {"gold coin": 42, "rope": 1}
dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]



def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        if addedItems[i] in inventory.keys():
            inventory[addedItems[i]] = inventory[addedItems[i]] + 1
        else:
            inventory[addedItems[i]] = 1
    return inventory

inv = addToInventory(inv, dragonLoot)

def displayInventory(inventory):
    print("Inventory: ")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + " " + str(k))
        item_total = item_total + v
    print("Total number of items: " + str(item_total))

displayInventory(inv)
