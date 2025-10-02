#Tyler Harris, I didn't add anything special that wasn't in the requirements
import os
cafeName = "Blues"
taxRate = .095
quanties = []
itemsList = [] 
itemPrice = []
discountCode = "STUDENT10"
sum = 0.0
tax = 0.0
subtotal = 0.0
discount = 0.0

def computeSubTotal():
    global sum, itemsList, itemPrice, quanties, subtotal
    for i in range(len(itemsList)):
        sum += itemPrice[i] * quanties[i]
        sum = round(sum, 2)
        subtotal = sum


def computeTax():
    global sum, tax
    tax = sum * taxRate
    sum += tax
    tax = round(tax, 2)

def applyDiscount():
    global sum, discount
    maybeAddDiscount = input("Would you like to apply your discount? (Y/N) ")
    if maybeAddDiscount.upper() == "Y":
        addDiscount = input("What is the discount code? ")
        if addDiscount == "STUDENT10":
            discount = sum * .10
            sum -= discount
            discount = round(discount, 2)
        else:
            print("That is an invalid discount code")

def addItem():
    global itemsList, itemPrice
    os.system('cls')
    itemToAdd = input("Which item would you like to add? Type \"Done\" when finished. ")
    if itemToAdd.strip() == "":
        while itemToAdd.strip() == "":
            print("You can't add nothing to your cart!")
            itemToAdd = input("Which item would you like to add? Type \"Done\" when finished. ")
    itemPriceToAdd = float(input("Price? "))
    if itemPriceToAdd <= 0:
        while itemPriceToAdd <= 0:
            print("That isn't a price that's acceptable!")
            itemPriceToAdd = float(input("Price? "))
    quantiesToAdd = int(input("How many? "))
    if quantiesToAdd <= 0:
        while quantiesToAdd <= 0:
            print("That isn't a quantity that's acceptable!")
            quantiesToAdd = int(input("How many? "))
    while(itemToAdd.upper() != "DONE"):
        itemsList.append(itemToAdd)
        itemPrice.append(float(itemPriceToAdd))
        quanties.append(int(quantiesToAdd))
        itemToAdd = input("Which item would you like to add? Type \"Done\" when finished. ")
        if itemToAdd.upper() != "DONE":
            itemPriceToAdd = input("Price? ")
        if itemToAdd.upper() != "DONE":
            quantiesToAdd = input("How many? ")
    os.system('cls')
    print("--------------")
    print("This is the list of items you added")
    print(itemsList)
    print("--------------")
    computeSubTotal()
    
def removeItem():
    global itemsList, itemPrice, quanties, sum
    for i in range(len(itemsList)):
        print(f"{i + 1}. {itemsList[i]}")
    if itemsList != []:
        itemToDelete = int(input("Which item would you like to delete? "))
        sum -= itemPrice[int(itemToDelete) - 1] * quanties[int(itemToDelete) - 1]
        return itemsList.pop(int(itemToDelete) - 1), itemPrice.pop(itemToDelete - 1), quanties.pop(itemToDelete - 1), sum
    os.system('cls')
    print("--------------------------")
    print("There is nothing to remove.")
    print("--------------------------")

def viewCart():
    global itemsList, itemPrice, quanties, sum
    os.system('cls')
    maxValue = max(itemPrice)
    maxIndex = itemPrice.index(maxValue)
    for i in range(len(itemsList)):
        print(f"Item: {itemsList[i]} | Price: ${itemPrice[i]} | Quantity: {quanties[i]}.")
    print(f"Your most expensive item is: {itemsList[maxIndex]} at a price point of ${maxValue}")
    print(f"Your subtotal is: {sum}")
    exitCart = input("\nPress enter to exit...")
    os.system('cls')

def checkout():
    global sum
    os.system('cls')
    print(f"Subtotal: ${subtotal}")
    computeTax()
    applyDiscount()
    sum = round(sum, 2)
    os.system('cls')
    print("Reciept")
    print("------------------------")
    print(f"Subtotal: ${subtotal}")
    print(f"Tax: ${tax}")
    print(f"Discount: -{discount}")
    print(f"Your final total is ${sum}.")
    quit()
    

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