"""Calculator

    Small calculator app to demonstrate function returns and object referencing.
    """

# import the logo art
from art import logo as logo


def add(num1, num2):
    """Addition

    Add two numbers

    Args:
        num1 (int): first number to add
        num2 (int): second number to add

    Returns:
        int: sum of num1 + num2
    """
    return num1 + num2


def subtract(num1, num2):
    """Subtraction

    Subtract num2 from num1

    Args:
        num1 (int): number to subtract from (minuend)
        num2 (ubt): number to subtract (subtrahend)

    Returns:
        int: difference of num1 - num2
    """
    return num1 - num2


def muiltiply(num1, num2):
    """Multiply

    Multiply num1 by num 2

    Args:
        num1 (int): first factor of the equation
        num2 (int): second factor of the equation

    Returns:
        int: product of num1 * num2
    """
    return num1 * num2


def divide(num1, num2):
    """Divide

    Divide num1 by num2

    Args:
        num1 (int): dividend
        num2 (int): divisor

    Returns:
        float: quotient of num1 / num2
    """
    return num1 / num2


# dict of the operations available ("operation_symbol": <reference to the function object for the operation>)
operations = {
    "+": add,
    "-": subtract,
    "*": muiltiply,
    "/": divide
}


# display the artwork
print(logo)

# show the available operations
for symbol in operations:
    print(symbol)

# prompt for the two numbers and the operation symbol
num1 = int(input("What's the first number? "))
operation_symbol = input("Pick an operation from the list above: ")
num2 = int(input("What's the second number? "))

# create the operation function
calculation_function = operations[operation_symbol]
# perform the operation
answer = calculation_function(num1, num2)

# display the result
print(f'{num1} {operation_symbol} {num2} = {answer}')
