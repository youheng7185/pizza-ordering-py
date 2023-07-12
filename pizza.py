print("pizza ordering system lmao")

def menu():
    print("1. small pizza - $1")
    print("2. medium pizza - $2")
    print("3. large pizza - $3")
    print("4. checkout")
    print("enter number for each selection")

smallPizzaPrice = 1
mediumPizzaPrice = 2
largePizzaPrice = 3
totalPrice = 0

smallNum = 0
mediumNum = 0
largeNum = 0

def currentPrice():
    totalPrice = smallNum * smallPizzaPrice + mediumNum * mediumPizzaPrice + largeNum * largePizzaPrice
    print(totalPrice)

while True:
    menu()
    currentPrice()
    sizePizza = input("size:")

    if sizePizza == "1":
        smallNum += 1
    elif sizePizza == "2":
        mediumNum += 1
    elif sizePizza == "3":
        largeNum += 1
    elif sizePizza == "4":
        print("ending order")
        print("u bought",smallNum,"of small pizza,",mediumNum,"of medium pizza",largeNum,"of large pizza")
        print("total puchase is: ")
        currentPrice()
        break
    else:
        print("wrong value, reenter again lol")