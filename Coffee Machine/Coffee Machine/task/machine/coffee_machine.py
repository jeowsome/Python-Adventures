water = 400
milk = 540
beans = 120
cups = 9
money = 550


def take():
    global money
    print(f"\nI gave you ${money}\n")
    money = money - money


def check(u_water, u_milk, u_beans, add_money):
    global money, water, milk, beans, cups
    water = water - u_water
    milk = milk - u_milk
    beans = beans - u_beans
    money = money + add_money
    cups = cups - 1
    if water > 0 and milk > 0 and beans > 0 and cups > 0:
        print("I have enough resources!, making you a coffee!\n")
    else:
        water = water + u_water
        milk = milk + u_milk
        beans = beans + u_beans
        money = money - add_money
        cups = cups + 1
        if water - u_water <= 0:
            print("Sorry, not enough water!\n")
        if milk - u_milk <= 0:
            print("Sorry, not enough milk!\n")
        if beans - u_beans <= 0:
            print("Sorry, not enough coffee beans\n")
        if cups <= 0:
            print("Sorry, not enough cups!\n")


def fill():
    global water, milk, cups, beans
    water += int(input("Write how many ml of water do you want to add:\n"))
    milk += int(input("Write how many ml of milk do you want to add:\n"))
    beans += int(input("Write how many grams of coffee beans do you want to add:\n"))
    cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))
    print()


def coffee_machine():
    if money != 0:
        print(f'''\nThe coffee machine has:
{water} of water
{milk} of milk
{beans} of coffee beans
{cups} of disposable cups
${money} of money\n''')
    else:
        print(f'''\nThe coffee machine has:
{water} of water
{milk} of milk
{beans} of coffee beans
{cups} of disposable cups
{money} of money\n''')


def buy():
    global water, beans, money, milk, cups, brewing
    flavor = input("\nWhat do you want to buy? 1 - espresso, 2 latte, 3 - cappuccino, back - to main menu:\n")

    if flavor == "1":  # espresso
        check(250, 0, 16, 4)
    elif flavor == "2":  # latte
        check(350, 75, 20, 7)
    elif flavor == "3":  # cappuccino
        check(200, 100, 12, 6)
    elif flavor == "back":
        brewing = True


def coffeemaker(opt):
    global brewing
    if opt == 'buy':
        buy()
    elif opt == "fill":
        fill()
    elif opt == "take":
        take()
    elif opt == 'remaining':
        coffee_machine()
    elif opt == 'exit':
        brewing = False


brewing = True

while brewing:
    option = input("Write action (buy, fill, take, remaining, exit):\n")
    coffeemaker(option)
