from sys import argv, stderr


"""
The program takes a string as an argument and encodes it into Morse Code.

It supports space and alphanumeric characters.
An alphanumeric character is represented by dots '.' and dashes '-'.
Complete morse characters are separated by a single space.
A space character is represented by a slash '/'.
"""


def get_morse() -> None:
    """Return a dictionary containing each character in the following form:
    <ascii char>: <morse equivalent>
    """
    return {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----."
    }


def convert_to_morse():
    args = argv[1:]   # Exclude the script name
    args_len = len(args)  # Get the number of arguments

    if args_len != 1:
        raise AssertionError("the arguments are bad")

    # The string to convert is the first arg
    string_to_convert = args[0]

    # Check if all characters are handled
    for char in string_to_convert:
        if not char.isalnum():
            raise AssertionError("the arguments are bad")

    morse = get_morse()  # Get the Morse Code dictionary
    string_len = len(string_to_convert) - 1

    # enumerate() gives the current index and the character while iterating.
    for i, char in enumerate(string_to_convert):
        if (i != string_len):  # If not the last char
            print(morse[char.upper()], end="")
        else:  # Don't print the space after the last Morse character
            print(morse[(char.upper())][:-1])


if __name__ == "__main__":
    try:
        convert_to_morse()
    except Exception as e:
        print(f"AssertionError: {e}", file=stderr)
