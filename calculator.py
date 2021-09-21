# day 10 project

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
num1 = int(input("Enter first number: "))
for symbol in operation:
    print(symbol)
# enter operator
operation_symbol = input("Enter any one of the above symbols: ")
# enter second number
num2 = int(input("Enter second number: "))

calculation_function = operation[operation_symbol]  # variable is assigned to a function
answer = calculation_function(num1, num2)    # now we pass parameters into that function

print(f"{num1} {operation_symbol} {num2} = {answer}")
