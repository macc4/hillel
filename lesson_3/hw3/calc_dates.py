from datetime import datetime

a = 0  # just a one-time variable so the program won't type the list of the commands all the time


def command_input():  # command input checked
    command_input.input = input("Choose your command: ")
    if command_input.input not in ('now', '-'):
        print('\nATTENTION! Please, use only one of the available commands!')
        print('(now, -)\n')
        command_input()


def input1():  # input 1 and 2 checked for value
    try:
        input1.first_input = datetime.strptime(input("Choose first date: "), "%d.%m.%Y")
    except ValueError:
        print('\nATTENTION! Please, use DD.MM.YYYY format!')
        input1()


def input2():
    try:
        input2.second_input = datetime.strptime(input('Choose second date: '), "%d.%m.%Y")
    except ValueError:
        print('\nATTENTION! Please, use DD.MM.YYYY format!')
        input2()


def c_dates():
    global a
    if a == 0:  # checking whether the list of the commands was typed already or not
        print('\nHere is the list of available commands:')
        print('use "now" to check the date')
        print('use "-" to calculate the difference between 2 dates')
        print('ATTENTION! Use DD.MM.YYYY format\n')
        a = a + 1

    command_input()
    if command_input.input == 'now':
        print(datetime.now())
    else:
        input1()
        input2()
        output = input1.first_input - input2.second_input
        print('\nThe difference is {} \n' .format(output))
    c_dates()
