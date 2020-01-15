print(' 7 8 9  / \n 4 5 6  * \n 1 2 3  - \n 0   C  +\n')

MASTER_RESULT = None #used for creating the loop

#input 1 and 2 checked for value
def input1():
    try:
        input1.first_input = float(input("Choose first number: "))
    except ValueError:
        print('ATTENTION! Please, use only numbers!\n')
        input1()

def input2():
    try:
        input2.second_input = float(input('You want to calculate: \n\n{} {} '.format(calculate.master, command_input.input)))
    except ValueError:
        print('ATTENTION! Please, use only numbers!\n')
        input2()

#command input checked
def command_input():
    command_input.input = input("Choose your command (you may choose from + - * /). You can also write C to delete the first input: ")
    if command_input.input not in ('+','-','*','/','C'):
        print('ATTENTION! Please, use only one of the available commands!\n')
        command_input()

#available commands
def add():
    global MASTER_RESULT
    result = calculate.master + input2.second_input
    MASTER_RESULT = result

def subtract():
    global MASTER_RESULT
    result = calculate.master - input2.second_input
    MASTER_RESULT = result

def multiply():
    global MASTER_RESULT
    result = calculate.master * input2.second_input
    MASTER_RESULT = result

def divide():
    global MASTER_RESULT
    try:
        result = calculate.master / input2.second_input
    except ZeroDivisionError: #zero division error checked
        print("You cannot divide by zero!")
        input2()
        divide()
        result = calculate.master / input2.second_input
    MASTER_RESULT = result

#main calculate loop
def calculate():
    global MASTER_RESULT
    if MASTER_RESULT == None: #checking whether input 1 is required or not
        input1()
        calculate.master = input1.first_input
    else:
        calculate.master = MASTER_RESULT

    command_input()
    if command_input.input == 'C':
        MASTER_RESULT = None
        calculate()

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

while True:
    calculate()