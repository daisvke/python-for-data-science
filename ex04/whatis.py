import sys

# Get args
args = sys.argv[1:]  # Exclude the script name
# Check if there is more than one argument
args_len = len(args)

if args_len < 1:
    sys.exit()
if args_len > 1:
    raise AssertionError("more than one argument is provided")

# Try to convert the argument to an integer
try:
    num = int(args[0])
except ValueError:
    raise AssertionError("argument is not an integer")
    sys.exit(1)

# Determine if the number is odd or even
if num % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
