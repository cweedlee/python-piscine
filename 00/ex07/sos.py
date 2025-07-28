import sys


def main():
    """
    program that takes a string as an argument and encodes it into Morse Code.
    • The program supports space and alphanumeric characters
    • An alphanumeric character is represented by dots . and dashes -
    • Complete morse characters are separated by a single space
    • A space character is represented by a slash /
    """
    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
        return 1
    morse = {" ": "/", "a": ".-", "b": "-...", "c": "-.-.", "d": "-..",
             "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..",
             "j": ".---", "k": "  -.-", "l": ".-..", "m": "--", "n": "-.",
             "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...",
             "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
             "y": "-.--", "a": ".-", "b": "-...", "c": "-.-.", "d": "-..",
             "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..",
             "j": ".---", "k": "  -.-", "l": ".-..", "m": "--", "n": "-.",
             "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...",
             "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
             "y": "-.--", "z": "--..", "z": "--.."}
    try:
        res = [morse[c] for c in sys.argv[1]]
    except KeyError:
        print("AssertionError: the arguments are bad")
        return 1
    length = len(res)
    for i in range(length):
        if (i < length - 1):
            print(res[i], end=" ")
        else:
            print(res[i])
    return 0


if __name__ == "__main__":
    main()
