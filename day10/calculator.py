
def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def muiltiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


operations = {
    "+": add,
    "-": subtract,
    "*": muiltiply,
    "/": divide
}

for symbol in operations:
    print(symbol)

num1 = int(input("What's the first number? "))
operation_symbol = input("Pick an operation from the list above: ")
num2 = int(input("What's the second number? "))

calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f'{num1} {operation_symbol} {num2} = {answer}')
