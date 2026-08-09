import sys


def morse(text):
    """
    This method is for getting morse code from actual source text.
    """
    NESTED_MORSE = {
        'A': '.- ',    'B': '-... ',  'C': '-.-. ',  'D': '-.. ',
        'E': '. ',     'F': '..-. ',  'G': '--. ',   'H': '.... ',
        'I': '.. ',    'J': '.--- ',  'K': '-.- ',   'L': '.-.. ',
        'M': '-- ',    'N': '-. ',    'O': '--- ',   'P': '.--. ',
        'Q': '--.- ',  'R': '.-. ',   'S': '... ',   'T': '- ',
        'U': '..- ',   'V': '...- ',  'W': '.-- ',   'X': '-..- ',
        'Y': '-.-- ',  'Z': '--.. ',

        'a': '.- ',    'b': '-... ',  'c': '-.-. ',  'd': '-.. ',
        'e': '. ',     'f': '..-. ',  'g': '--. ',   'h': '.... ',
        'i': '.. ',    'j': '.--- ',  'k': '-.- ',   'l': '.-.. ',
        'm': '-- ',    'n': '-. ',    'o': '--- ',   'p': '.--. ',
        'q': '--.- ',  'r': '.-. ',   's': '... ',   't': '- ',
        'u': '..- ',   'v': '...- ',  'w': '.-- ',   'x': '-..- ',
        'y': '-.-- ',  'z': '--.. ',

        '0': '----- ', '1': '.---- ', '2': '..--- ', '3': '...-- ',
        '4': '....- ', '5': '..... ', '6': '-.... ', '7': '--... ',
        '8': '---.. ', '9': '----. ',

        ' ': '/ '
    }
    res = ""

    for c in text:
        if not c.isalnum() and not c == ' ':
            raise AssertionError("the arguments are bad")
        res += NESTED_MORSE[c]
    print(res)


def main():
    """
    Gets input from the terminal, validates and calls the morse method on it.
    """
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        morse(sys.argv[1])
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if (__name__ == "__main__"):
    main()
