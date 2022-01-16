from simpleeval import simple_eval

count = 2
variable_count = input('Enter element count:')
operations = ['+', '-', '*', '/', '//', '**']


def calculate(expr):
    result = expr
    try:
        result = simple_eval(expr)
    except ZeroDivisionError as err:
        print(f'You cannot divide by zero. Error type {err}')
        exit(1)
    return result


def check_operation(operator):
    if operator not in operations:
        print('Operation was not found.')
        exit(1)


def parse_user_input(user_input):
    val = user_input
    try:
        val = float(user_input)
    except ValueError:
        print(f"No.. input is not a number. It's a string, input value was {val}.")
        exit(1)
    return val


variable_count = parse_user_input(variable_count)
var_1 = input(f'Enter var1:')
parse_user_input(var_1)

operation = input(f'Enter operation1:')
check_operation(operation)

var_2 = input(f'Enter var2:')
parse_user_input(var_2)
expression = f'{var_1}{operation}{var_2}'

if variable_count > 2:
    while count < variable_count:
        operation = input(f'Enter operation{count}:')
        check_operation(operation)

        var = input(f'Enter var{count + 1}:')
        parse_user_input(var)

        expression = f'{expression}{operation}{var}'
        count += 1

print('Result:', calculate(expression))
