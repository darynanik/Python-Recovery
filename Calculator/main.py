from simpleeval import simple_eval
count = 2
inputs = []
variable_count = input('Enter element count:')

operations = ['+', '-', '*', '/']

def calculate(expr):
    try:
        result = simple_eval(expr)
    except ZeroDivisionError as err:
        print(f'You cannot divide by zero. Error type {err}')
        exit(0)
    return result   
def check_operation(operation):
    if operation not in operations:
        print('Operation was not found.')
        exit(0)          
def check_user_input(input):
    val = input
    try:
        # Convert it into integer
        val = int(input)
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
        except ValueError:
            print(f"No.. input is not a number. It's a string, input value was {val}.")
            exit(0)
    return val

expression = ''
variable_count = check_user_input(variable_count)
var_1 =   input(f'Enter var1:')
check_user_input(var_1)

operation = input(f'Enter operation1:')
check_operation(operation)

var_2 =  input(f'Enter var2:')
check_user_input(var_2)
inputs.extend([var_1, operation, var_2])
expression = expression.join(inputs)

if variable_count > 2:
    while count < variable_count:
        operation = input(f'Enter operation{count}:')
        check_operation(operation)
         
        var = input(f'Enter var{count+1}:')
        check_user_input(var)
        
        inputs.extend([operation, var])
        expression = ''.join(inputs)
        count += 1
 
print('Result:', calculate(expression))