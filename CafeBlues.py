import os
cafeName = "Blues"
taxRate = 9.5
items = ['Black Coffee', 'Caramel Cappicheno', 'Rainbow Swirl', 'Chocolate Brownie', 'Apple Cinnamon']
prices = [3.25, 6.25, 6.75, 6.50, 6.25]
quanties = []
itemsList = [] 
discountCode = "STUDENT10"

def addItem():
    global itemsList, quanties
    os.system('cls')
    print("This is our menu!")
    print("------------------")
    for i in range(len(items)):
        print(f"{i + 1}. {items[i]}")
    print("------------------")
    itemToAdd = input("Which item would you like to add? Type \"Done\" when finished. ")
    while(itemToAdd.upper() != "DONE"):
        itemsList.append(items[int(itemToAdd) - 1])
        itemToAdd = input("Which item would you like to add? Type \"Done\" when finished. ")
    print(itemsList)
    
def viewCart():
    global itemsList, quanties
    os.system('cls')
    for i in range(len(itemsList)):
        print(f"{i + 1}. {itemsList[i]}")
    exitCart = input("\nPress enter to exit...")
    os.system('cls')
def removeItem():
    global itemsList
    for i in range(len(itemsList)):
        print(f"{i + 1}. {itemsList[i]}")
    print(itemsList)
    itemToDelete = int(input("Which item would you like to delete? "))
    return itemsList.pop(int(itemToDelete) - 1)
def checkout():
    global itemsList, discountCode
    print()

def mainMenu():
    number = int(input("Which number would you like to pick? "))
    while number != 0 and number != 5:
        if number == 1:
            addItem()
        elif number == 2:
            viewCart()
        elif number == 3:
            removeItem()
        elif number == 4:
            checkout()
        showBanner()
        number = int(input("Which number would you like to pick? "))
    print("Goodbye...")


def showBanner():
    print(f"Welcome to Cafe {cafeName}! Our tax rate is {taxRate}%.")
    print("---------------")
    print("1. Add Item")
    print("2. View Cart")
    print("3. Remove Item by Number")
    print("4. Checkout")
    print("5. Quit")
    print("---------------")

def main():
    showBanner()
    mainMenu()

main()