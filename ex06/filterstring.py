import sys
from ft_filter import ft_filter


def filterstring() -> None:
    """Filter the string and print the resulting list"""
    args = sys.argv[1:]   # Exclude the script name
    args_len = len(args)  # Get the number of arguments

    if args_len != 2:
        raise AssertionError("the arguments are bad")

    # Get the arguments
    string, nbr = args

    try:  # Convert the string number into an integer
        nbr = int(nbr)
    except ValueError:
        raise AssertionError("the arguments are bad")

    # Split the string to have a list of the words contained in the string
    string = string.split()

    # Using lambda function to pass 'nbr' as ft_filter takes only 1 arg
    filtered_string = ft_filter(lambda s: len(s) > nbr, string)

    print(filtered_string)


if __name__ == "__main__":
    try:
        filterstring()
    except Exception as e:
        print(f"AssertionError: {e}", file=sys.stderr)
