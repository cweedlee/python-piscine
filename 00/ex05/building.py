import sys
import string


def countTypeAmount(msg, f) -> int:
    res = 0
    for c in msg:
        if f(c) is True:
            res = res + 1
    return res


def main():
    """
    This function takes 1 argument
    analyze the characters into several types :
    - upper letters
    - lower letters
    - punctuation marks
    - spaces
    - digits
    """

    # check argv
    if len(sys.argv) > 2:
        print("AssertionError: too many arguments")

    msg = ""

    if len(sys.argv) == 1:
        msg = str(input("What is the text to count?\n"))
    else:
        msg = sys.argv[1]

    print(f"The text contains {len(msg)} characters:")
    print(f"{countTypeAmount(msg, isUpper)} upper letters")
    print(f"{countTypeAmount(msg, isLower)} lower letters")
    print(f"{countTypeAmount(msg, isPunc)} punctuation marks")
    print(f"{countTypeAmount(msg, isSpace)} spaces")
    print(f"{countTypeAmount(msg, isDigit)} digits")


def isUpper(c):
    return c.isupper()


def isLower(c):
    return c.islower()


def isPunc(c):
    return any(c == p for p in string.punctuation)


def isSpace(c):
    return c.isspace()


def isDigit(c):
    return c.isdigit()


if __name__ == "__main__":
    main()
