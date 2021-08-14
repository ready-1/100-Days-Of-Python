from os import system, name, truncate


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def prime_checker(number):
    is_prime = True
    i = number - 1
    while is_prime == True and i > 1:
        if number % i == 0:
            is_prime = False
        i -= 1
    return is_prime


clear()
number = int(input("Enter a number: "))

if prime_checker(number):
    print("It's a prime number.")
else:
    print("It's not a prime number.")
