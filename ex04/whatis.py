import sys


def odd_or_even(args: list, args_len: int) -> None:
    # If no argument is given, we quit quietly
    if args_len < 1:
        sys.exit()
    if args_len > 1:
        raise AssertionError("more than one argument is provided")

    # Try to convert the argument to an integer
    try:
        num = int(args[0])
    except ValueError:
        raise AssertionError("argument is not an integer")

    # Determine if the number is odd or even
    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


# Get args from command line
args = sys.argv[1:]  # Exclude the script name
# Check if there is more than one argument
args_len = len(args)

try:
    odd_or_even(args, args_len)
except Exception as e:
    print(f"AssertionError: {e}", file=sys.stderr)
