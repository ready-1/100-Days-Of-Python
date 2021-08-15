from os import system, name


def clear():
    """Clear the screen

    Use the system clear command to clear the terminal screen.
    This does not clear the history or scrollback.
    """
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
