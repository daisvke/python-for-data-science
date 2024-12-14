import argparse
import sys

# Init parser
parser = argparse.ArgumentParser()

# Add arg to parser
parser.add_argument(
    "number", type=str, nargs='?',
    help="The number to check whether it is odd or even.",
    )

# Parse args
args = parser.parse_args()

# Check if there is more than one argument
args_len = len(vars(args))

if args_len <= 1: sys.exit()
if args_len > 1:
    raise AssertionError("more than one argument is provided")

# Try to convert the argument to an integer
try:
    num = int(args.number)
except ValueError:
    raise AssertionError("argument is not an integer")

# Determine if the number is odd or even
if num % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
