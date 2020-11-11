water_amount = 400
milk_amount = 540
cbeans_amount = 120
disposable_cups = 9
money_amount = 550


def display_content():
    print("The coffee machine has:")
    print(water_amount, "of water")
    print(milk_amount, "of milk")
    print(cbeans_amount, "of coffee beans")
    print(disposable_cups, "of disposable cups")
    print(money_amount, "of money")


def resource_checker():
    option_selector = input("What do you want to buy? 1 - espresso, 2 - latte,"
                            " 3 - cappuccino, back:")

    if option_selector == "back":
        return None
    elif disposable_cups < 1:
        coffee_ordered = "disposable cups"
    elif option_selector == "1":
        if water_amount < 250:
            coffee_ordered = "water"
        elif cbeans_amount < 16:
            coffee_ordered = "coffee beans"
        else:
            coffee_ordered = option_selector
    elif option_selector == "2":
        if water_amount < 350:
            coffee_ordered = "water"
        elif milk_amount < 75:
            coffee_ordered = "milk"
        elif cbeans_amount < 20:
            coffee_ordered = "coffee beans"
        else:
            coffee_ordered = option_selector
    else:
        if water_amount < 200:
            coffee_ordered = "water"
        elif milk_amount < 100:
            coffee_ordered = "milk"
        elif cbeans_amount < 12:
            coffee_ordered = "coffee beans"
        else:
            coffee_ordered = option_selector
    make_coffee(coffee_ordered)


def make_coffee(coffee_ordered):
    global water_amount, milk_amount, cbeans_amount, disposable_cups, money_amount

    if coffee_ordered == "1":
        print("I have enough resources, making you a coffee!")
        water_amount -= 250
        cbeans_amount -= 16
        disposable_cups -= 1
        money_amount += 4
    elif coffee_ordered == "2":
        print("I have enough resources, making you a coffee!")
        water_amount -= 350
        milk_amount -= 75
        cbeans_amount -= 20
        disposable_cups -= 1
        money_amount += 7
    elif coffee_ordered == "3":
        print("I have enough resources, making you a coffee!")
        water_amount -= 200
        milk_amount -= 100
        cbeans_amount -= 12
        disposable_cups -= 1
        money_amount += 6
    else:
        print("Sorry, not enough", coffee_ordered)


def fill_machine():
    global water_amount, milk_amount, cbeans_amount, disposable_cups

    water_fill = int(input("Write how many ml of water do you want to add:"))
    milk_fill = int(input("Write how many ml of milk do you want to add:"))
    cbeans_fill = int(
        input("Write how many grams of coffee beans do you want to add:"))
    dcups_fill = int(
        input("Write how many disposable cups of coffee do you want to add:"))

    water_amount += water_fill
    milk_amount += milk_fill
    cbeans_amount += cbeans_fill
    disposable_cups += dcups_fill


def give_money():
    global money_amount
    print("I gave you $" + str(money_amount))
    money_amount = 0


def main():
    while True:
        task = input("Write action (buy, fill, take, remaining, exit):")
        if task == "buy":
            resource_checker()
        elif task == "fill":
            fill_machine()
        elif task == "remaining":
            display_content()
        elif task == "exit":
            break
        else:
            give_money()
    return None


main()
