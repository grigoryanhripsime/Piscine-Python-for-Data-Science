import sys
import string


def calc_symbols(user_input):
    """
    This method printh the overall number of characters and
    then number of upper, lower cased characters,
    punctuation marks, spaces and digits.
    """
    upper_cases = sum(1 for c in user_input if c.isupper())
    lower_cases = sum(1 for c in user_input if c.islower())
    punctuation_marks = sum(1 for c in user_input if c in string.punctuation)
    spaces = sum(1 for c in user_input if c.isspace())
    digits = sum(1 for c in user_input if c.isdigit())

    print(f"The text contains {len(user_input)} characters:")
    print(f"{upper_cases} upper cases")
    print(f"{lower_cases} lower cases")
    print(f"{punctuation_marks} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    """
    The program waits for input.
    If the number of arguments is more then required, we raise exception.
    If only one argument is sent we count and display the chars count.
    If no imput, just ask for it.
    """
    try:
        if len(sys.argv) > 2:
            raise AssertionError("Too many arguments provided")
        if len(sys.argv) == 1:
            try:
                text = input("What is the text to count?\n")
            except Exception:
                return
        else:
            text = sys.argv[1]
        calc_symbols(text)
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()
