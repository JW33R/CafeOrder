#Tyler Harris, I added something that doesn't allow the user to use the remove function if there is nothing to remove
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
    #Takes the the itemPrice and quantity and multplies them and adds them to the sum to create the subtotal
    global sum, itemsList, itemPrice, quanties, subtotal
    for i in range(len(itemsList)):
        sum += itemPrice[i] * quanties[i]
        sum = round(sum, 2)
        subtotal = sum


def computeTax():
    #Takes the sum and multiplies it by the taxrate which is .095 to get the total tax on the item
    global sum, tax
    tax = sum * taxRate
    sum += tax
    tax = round(tax, 2)

def applyDiscount():
    #Asks the user if they want a discount and if they do they can enter the code and if they get it wrong they don't get another chance to try again. If they enter the code it takes off 10%
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
    #Asks the user to add an item and if they enter nothing or spaces then it has them try again until they enter a valid answer
    itemToAdd = input("Which item would you like to add? Type \"Done\" when finished. ")
    if itemToAdd.strip() == "":
        while itemToAdd.strip() == "":
            print("You can't add nothing to your cart!")
            itemToAdd = input("Which item would you like to add? Type \"Done\" when finished. ")
    #Asks the user to add a price to the item and if they enter a negative or 0 then they have to keep trying until they enter a positive int
    itemPriceToAdd = float(input("Price? "))
    itemPriceToAdd = round(itemPriceToAdd, 2)
    if itemPriceToAdd <= 0:
        while itemPriceToAdd <= 0:
            print("That isn't a price that's acceptable!")
            itemPriceToAdd = float(input("Price? "))
            itemPriceToAdd = round(itemPriceToAdd, 2)
    #Asks the user to enter how many of that item they want and if they don't enter more then 0 then it will make them try until they enter a correct number
    quantiesToAdd = int(input("How many? "))
    if quantiesToAdd <= 0:
        while quantiesToAdd <= 0:
            print("That isn't a quantity that's acceptable!")
            quantiesToAdd = int(input("How many? "))
    #Checks to see if the user put the word done into the item list and if not then adds all of the answers they entererd to their respective lists and asks them again
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
    global itemsList, itemPrice, quanties, sum, subtotal
    #Prints the list of items the user entered previously and deletes the item they wanted to delete if there are no items in the list it doesn't allow them to delete anything
    os.system('cls')

    for i in range(len(itemsList)):
        print(f"{i + 1}. {itemsList[i]}")
    
    if itemsList != []:
        itemToDelete = int(input("Which item would you like to delete? "))
        sum -= itemPrice[int(itemToDelete) - 1] * quanties[int(itemToDelete) - 1]
        subtotal -= itemPrice[int(itemToDelete) - 1] * quanties[int(itemToDelete) - 1]
        os.system('cls')
        return itemsList.pop(int(itemToDelete) - 1), itemPrice.pop(itemToDelete - 1), quanties.pop(itemToDelete - 1), sum
    
    os.system('cls')
    print("--------------------------")
    print("There is nothing to remove.")
    print("--------------------------")

def viewCart():
    global itemsList, itemPrice, quanties, sum
    #Grabs the max price at the index the max price was at then prints each item, price, and quantity along with the most expensive item and their subtotal
    os.system('cls')
    if itemPrice != []:
        maxValue = max(itemPrice)
        maxIndex = itemPrice.index(maxValue)

        for i in range(len(itemsList)):
            print(f"Item: {itemsList[i]} | Price: ${itemPrice[i]} | Quantity: {quanties[i]}.")
    
        print(f"Your most expensive item is: {itemsList[maxIndex]} at a price point of ${maxValue}")
        print(f"Your subtotal is: ${sum}")
        exitCart = input("\nPress enter to exit...")
        os.system('cls')
    else:
        print("--------------")
        print("Your cart is empty!")
        print("--------------")

def checkout():
    global sum
    #Prints a recipet of the users subtotal, tax, discount if they had one and their final total then quits the program
    os.system('cls')
    if itemsList != []:
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
    else:
        print("---------------")
        print("How can you check out with no items?")
        print("---------------")
    

def mainMenu():
    #Goes through a loop of the main menu to see what the user would like to pick
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
    #This is the function that shows the main menu
    print(f"Welcome to Cafe {cafeName}! Our tax rate is {taxRate}%.")
    print("---------------")
    print("1. Add Item")
    print("2. View Cart")
    print("3. Remove Item by Number")
    print("4. Checkout")
    print("5. Quit")
    print("---------------")

def main():
#Self-explainatory
    showBanner()
    mainMenu()

main()