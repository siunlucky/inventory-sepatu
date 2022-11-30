items = {"Nike": {"s10": 3, "s11": 1, "s12": 3},
         "Adidas": {"s10": 3, "s11": 1, "s12": 3},
         "Princes": {"s10": 3, "s11": 1, "s12": 3}}


def main():
    print("WELCOME TO INVENTORY MANAGEMENT")
    print("-------------------------------")
    print()
    print("Available Options:")
    print()
    print("1 - Add Items To Inventory")
    print("2 - View Inventory")
    print()
    while True:
        userChoice = input("Choose An Option: ")
        if userChoice == '1':
            addItemToInventory()
            break
        elif userChoice == '2':
            viewInventory()
            break


def addItemToInventory():
    print("ADD ITEMS TO INVENTORY")
    print("----------------------")
    print()
    while True:
        userItem = input("Item Name: ")
        if userItem != '':
            break
    while True:
        itemSize = input("Item Size: ")
        if itemSize.isdigit():
            break
    while True:
        itemAmount = input("Item Amount: ")
        if itemAmount.isdigit():
            break
    itemsArray = {userItem: {"s" + itemSize: itemAmount}}
    items.update(itemsArray)
    returnToMainMenu("Your item has been added!")


def viewInventory():
    print("VIEW INVENTORY")
    print("--------------")
    print()
    print("ITEMS")
    print("-----")
    print()
    for item in items:
        print(item)
        for size in items[item]:
            print("Size", size.split('s', 1)[
                  1], ", Total :", items[item][size])
        print()
    print()
    print("Available Options:")
    print()
    print("1 - Edit Item")
    print("2 - Delete Item")
    print()
    while True:
        userChoice = input("Choose An Option: ")
        if userChoice == '1':
            editInventoryItem()
            break
        elif userChoice == '2':
            deleteInventoryItem()
            break


def editInventoryItem():
    print("EDIT INVENTORY ITEM")
    print("-------------------")
    print("Press (B) To Go Back")
    print()
    print("Available Options")
    print()
    print("1 - Edit Item Name")
    print("2 - Edit Size")
    print("3 - Edit Item Amount")
    print()
    while True:
        userChoice = input("Choose An Option: ").lower()
        if userChoice in ['1', '2', '3', 'b']:
            break
    if userChoice == 'b':
        main()

    if userChoice == '1':
        print()
        while True:
            itemToChange = input("Enter The Name Of The Item To Edit: ")
            if itemToChange in items:
                break
            else:
                print("That Item Does Not Exist")
                print()

        while True:
            newItemName = input("Enter The New Item Name: ")
            if newItemName != '':
                break
        items.update({newItemName: items[itemToChange]})
        del items[itemToChange]

        returnToMainMenu("Item Name Has Been Changed")

    if userChoice == '2':
        print()
        while True:
            itemToChange = input("Enter The Name Of The Item To Edit: ")
            if itemToChange in items:
                break
            else:
                print("That Item Does Not Exist")
                print()

        while True:
            sizeToChange = "s" + input("Enter The Size Of The Item To Edit: ")
            if sizeToChange in items[itemToChange]:
                break
            else:
                print("That Size Does Not Exist")
                print()
        while True:
            newItemSize = "s" + input("Enter The New Item Size: ")
            if newItemSize != '':
                if newItemSize in items[itemToChange]:
                    print("That Size already Exist!")
                    print()
                else:
                    break

        items[itemToChange].update(
            {newItemSize: items[itemToChange][sizeToChange]})
        del items[itemToChange][sizeToChange]

        returnToMainMenu("Item Size Has Been Changed")

    if userChoice == '3':
        print()
        while True:
            itemToChange = input("Enter The Name Of The Item To Edit: ")
            if itemToChange in items:
                break
            else:
                print("That Item Does Not Exist")
                print()

        while True:
            sizeToChange = "s" + input("Enter The Size Of The Item To Edit: ")
            if sizeToChange in items[itemToChange]:
                break
            else:
                print("That Size Does Not Exist")
                print()
        while True:
            newAmountItem = input("Enter The New Item Amount: ")
            if newAmountItem != '':
                break

        items[itemToChange].update({sizeToChange: newAmountItem})

        returnToMainMenu("Item Amount Has Been Changed")


def deleteInventoryItem():
    print("DELETE INVENTORY ITEM")
    print("---------------------")
    print()
    while True:
        itemToDelete = input("Enter The Name Of The Item To Delete: ")
        if itemToDelete in items:
            break
        else:
            print("That Item Does Not Exist")
            print()

    while True:
        confirmation = input(
            "CONFIRMATION: Are You Sure You Want To Delete This Item: ").lower()
        if confirmation in ['yes', 'no']:
            break
    if confirmation == 'yes':
        del items[itemToDelete]
        returnToMainMenu("Item Has Been Deleted")
    else:
        main()


def returnToMainMenu(message):
    while True:
        print()
        back = input(f"{message}. Press (M) To Return To Main Menu: ").lower(
        ) if message != None else input("Press (M) To Return To Main Menu: ").lower()
        if back == 'm':
            main()
            break


main()
