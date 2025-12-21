import sys
from ft_filter import ft_filter


def main():
    """
This main method gets arguments from terminal and prints all the
strings from S that are longer than mentiones N number.
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        try:
            N = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        print(ft_filter(lambda S: len(S) > N, sys.argv[1].split(" ")))
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if (__name__ == "__main__"):
    main()
