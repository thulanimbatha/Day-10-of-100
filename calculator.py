# day 10 project

exit_calc = False

# add function
def add(num1, num2):
    '''Returns sum of two numbers'''
    return num1 + num2

# subtraction function
def subtract(num1, num2):
    '''Returns subtraction of two numbers'''
    return num1 - num2

# multiplication function
def mult(num1, num2):
    '''Returns product of two numbers'''
    return num1 * num2

# division function
def div(num1, num2):
    '''Returns division of two numbers'''
    return num1 / num2

# dictionary
operation = {
    "+" : add,
    "-" : subtract,
    "*" : mult,
    "/" : div,
}
# enter first number
num1 = float(input("Enter first number: "))
for symbol in operation:
    print(symbol)

while not exit_calc:
    # enter operator
    operation_symbol = input("Enter an operation: ")
    # enter second number
    num2 = float(input("Enter next number: "))

    calculation_function = operation[operation_symbol]  # variable is assigned to a function
    answer = calculation_function(num1, num2)    # now we pass parameters into that function
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input("Continue operation ('y' or 'n')? ") == "y":
        num1 = answer
    else:
        print("Goodbye! Shutting down....")
        exit_calc = True

'''ADD WHILE LOOP & RECURSION'''
