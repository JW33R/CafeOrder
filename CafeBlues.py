import os
from collections import Counter
cafeName = "Blues"
taxRate = .095
quanties = []
itemsList = [] 
itemPrice = []
discountCode = "STUDENT10"

def addItem():
    global itemsList, itemPrice
    os.system('cls')
    itemToAdd = input("Which item would you like to add? Type \"Done\" when finished. ")
    itemPriceToAdd = input("Price? ")
    while(itemToAdd.upper() != "DONE"):
        itemsList.append(itemToAdd)
        itemPrice.append(itemPriceToAdd)
        itemToAdd = input("Which item would you like to add? Type \"Done\" when finished. ")
        if itemToAdd.upper() != "DONE":
            itemPriceToAdd = input("Price? ")
    print(itemsList)
    
def viewCart():
    global itemsList, itemPrice
    os.system('cls')
    for i in itemsList:
        print(itemsList.count(i))
    for i in range(len(itemsList)):
        print(f"{itemsList[i]}. {itemPrice[i]}")
    exitCart = input("\nPress enter to exit...")
    os.system('cls')
def removeItem():
    global itemsList
    for i in range(len(itemsList)):
        print(f"{i + 1}. {itemsList[i]}")
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