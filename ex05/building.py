import sys
import string


def analyze_string(input_string: str) -> None:
    """Analyze the text and count the categories."""
    # This is a generator expression that produces a 1 for every character
    # in input_string that passes the condition char.isupper().
    upper_count = sum(1 for char in input_string if char.isupper())
    lower_count = sum(1 for char in input_string if char.islower())
    punctuation_count = sum(
        1 for char in input_string if char in string.punctuation
        )
    space_count = sum(1 for char in input_string if char.isspace())
    digit_count = sum(1 for char in input_string if char.isdigit())

    print(f"The text contains {len(input_string)} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


def main():
    # Get args
    args = sys.argv
    # Get args number
    args_len = len(args)

    if args_len == 1:  # If no arg is found, ask for the string to count
        print("What is the text to count?")
        string_to_count = sys.stdin.readline()
    elif args_len > 2:
        raise AssertionError("More than one argument is provided")
    else:  # Analyse the first argument
        string_to_count = args[1]

    analyze_string(string_to_count)


if __name__ == "__main__":
    main()
