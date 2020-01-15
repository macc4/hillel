MASTER_RESULT = None  # used for creating the loop


def input1():  # input 1 and 2 checked for value
    try:
        input1.first_input = float(input("Choose first number: "))
    except ValueError:
        print('ATTENTION! Please, use only numbers!\n')
        input1()


def input2():
    try:
        input2.second_input = float(input('You want to calculate: \n{} {} '.format(c_numbers.master, command_input.input)))
    except ValueError:
        print('ATTENTION! Please, use only numbers!\n')
        input2()


def command_input():  # command input checked
    command_input.input = input("Choose your command (you may choose from + - * /). You can also write C to delete the first input: ")
    if command_input.input not in ('+','-','*','/','C'):
        print('ATTENTION! Please, use only one of the available commands!\n')
        command_input()


def add():  # available commands
    global MASTER_RESULT
    result = c_numbers.master + input2.second_input
    MASTER_RESULT = result


def subtract():
    global MASTER_RESULT
    result = c_numbers.master - input2.second_input
    MASTER_RESULT = result


def multiply():
    global MASTER_RESULT
    result = c_numbers.master * input2.second_input
    MASTER_RESULT = result


def divide():
    global MASTER_RESULT
    try:
        result = c_numbers.master / input2.second_input
    except ZeroDivisionError: # zero division error checked
        print("You cannot divide by zero!")
        input2()
        divide()
        result = c_numbers.master / input2.second_input
    MASTER_RESULT = result


def c_numbers():  # main  c_numbers loop
    global MASTER_RESULT
    if MASTER_RESULT == None: # checking whether input 1 is required or not
        print('\n 7 8 9  / \n 4 5 6  * \n 1 2 3  - \n 0   C  +\n')
        input1()
        c_numbers.master = input1.first_input
    else:
        c_numbers.master = MASTER_RESULT

    command_input()
    if command_input.input == 'C':
        MASTER_RESULT = None
        c_numbers()

    input2()
    if command_input.input == '+':
        add()
        print('= {}\n'.format(MASTER_RESULT))
    elif command_input.input == '-':
        subtract()
        print('= {}\n'.format(MASTER_RESULT))
    elif command_input.input == '/':
        divide()
        print('= {}\n' .format(MASTER_RESULT))
    else:
        multiply()
        print('= {}\n' .format(MASTER_RESULT))
    c_numbers()
