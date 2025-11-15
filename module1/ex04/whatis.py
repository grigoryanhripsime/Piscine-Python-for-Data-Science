import sys

if len(sys.argv) == 1:
    sys.exit()
if len(sys.argv) > 2:
    print("AssertionError: more than one argument is provided")
    sys.exit()

try:
    n = int(sys.argv[1])
except ValueError:
    print("AssertionError: argument is not an integer")
    sys.exit()

print("I'm Even" if n % 2 == 0 else "I'm Odd")
