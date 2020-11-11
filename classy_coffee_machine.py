# ~
class CoffeeMachine:
    machine_state = "start"

    def __init__(self, water, milk, beans, cups, money):
        self.water_amount = water
        self.milk_amount = milk
        self.coffee_beans_amount = beans
        self.disposable_cups_amount = cups
        self.money_amount = money

    def input_processor(self, user_input):
        if self.machine_state == "start":
            # !display remaining here
            if user_input == "remaining":
                print("The coffee machine has:")
                print(self.water_amount, "of water")
                print(self.milk_amount, "of milk")
                print(self.coffee_beans_amount, "of coffee beans")
                print(self.disposable_cups_amount, "of disposable cups")
                print(self.money_amount, "of money")
            elif user_input == "buy":
                self.machine_state = "buying coffee"
            elif user_input == "fill":
                self.machine_state = "adding water"
            elif user_input == "take":
                # !give the moneh here
                print("I gave you $", self.money_amount)
                self.money_amount = 0
            elif user_input == "exit":
                self.machine_state = ""
            else:
                return None
        elif self.machine_state == "buying coffee":
            # !see input, check resources, give coffee (or not)
            # !all this in a very ugly probably not readable way, but let's see
            if user_input == "back":
                self.machine_state = "start"
                return None
            elif self.disposable_cups_amount < 1:
                print("Sorry, not enough disposable cups")
            elif user_input == "1":
                # !make an espresso here, after checking resources
                if self.water_amount < 250:
                    print("Sorry, not enough water")
                elif self.coffee_beans_amount < 16:
                    print("Sorry, not enough coffee beans")
                else:
                    print("I have enough resources, making you a coffee!")
                    self.water_amount -= 250
                    self.coffee_beans_amount -= 16
                    self.disposable_cups_amount -= 1
                    self.money_amount += 4
            elif user_input == "2":
                # !make a latte here
                if self.water_amount < 350:
                    print("Sorry, not enough water")
                elif self.milk_amount < 75:
                    print("Sorry, not enough milk")
                elif self.coffee_beans_amount < 20:
                    print("Sorry, not enough coffee beans")
                else:
                    print("I have enough resources, making you a coffee!")
                    self.water_amount -= 350
                    self.milk_amount -= 75
                    self.coffee_beans_amount -= 20
                    self.disposable_cups_amount -= 1
                    self.money_amount += 7
            elif user_input == "3":
                # !make a cappuccino here
                if self.water_amount < 200:
                    print("Sorry, not enough water")
                elif self.milk_amount < 100:
                    print("Sorry, not enough milk")
                elif self.coffee_beans_amount < 12:
                    print("Sorry, not enough coffee beans")
                else:
                    print("I have enough resources, making you a coffee!")
                    self.water_amount -= 200
                    self.milk_amount -= 100
                    self.coffee_beans_amount -= 12
                    self.disposable_cups_amount -= 1
                    self.money_amount += 6
            else:
                return None
            self.machine_state = "start"
        elif best_coffee_machine.machine_state == "adding water":
            # !probably a better way to make this but here it restocks on resources
            # !for every resource a different input has to be taken, hence the check changes after every resource added
            self.water_amount += int(user_input)
            self.machine_state = "adding milk"
        elif best_coffee_machine.machine_state == "adding milk":
            self.milk_amount += int(user_input)
            self.machine_state = "adding coffee beans"
        elif best_coffee_machine.machine_state == "adding coffee beans":
            self.coffee_beans_amount += int(user_input)
            self.machine_state = "adding disposable cups"
        elif self.machine_state == "adding disposable cups":
            self.disposable_cups_amount += int(user_input)
            self.machine_state = "start"

    def input_strings(self):
        if self.machine_state == "start":
            return "Write action (buy, fill, take, remaining, exit):"
        elif self.machine_state == "buying coffee":
            return "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back:"
        elif self.machine_state == "adding water":
            return "Write how many ml of water do you want to add:"
        elif self.machine_state == "adding milk":
            return "Write how many ml of milk do you want to add:"
        elif self.machine_state == "adding coffee beans":
            return "Write how many grams of coffee beans do you want to add:"
        elif self.machine_state == "adding disposable cups":
            return "Write how many disposable cups of coffee do you want to add:"
        else:
            return "How did we get here"


def main():
    while best_coffee_machine.machine_state:
        best_coffee_machine.input_processor(
            input(best_coffee_machine.input_strings()))


best_coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)

best_coffee_machine.input_processor(main())
