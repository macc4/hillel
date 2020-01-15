from calc_numbers import c_numbers
from calc_dates import c_dates


def choose_module():  # choosing the module
    choose_module.input = input("Hi! Do you want to calculate numbers or dates? ")
    if choose_module.input not in ('numbers', 'dates'):
        print('ATTENTION! Please, use only one of the available commands!\n(numbers, dates)')
        choose_module()


if __name__ == '__main__':
    choose_module()
    if choose_module.input == 'numbers':
        c_numbers()
    else:
        c_dates()
