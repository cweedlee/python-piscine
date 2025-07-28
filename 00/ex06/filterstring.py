import sys


def main():
    """
    Count the words that is longer than 2nd argv(integer)
    from 1st argv(string).
    argv:
        1. string : taken as the list of words
        2. integer : parameter for word length
    """
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
        return 1
    s = ""
    n = 0
    try:
        s = str(sys.argv[1])
        n = int(sys.argv[2])
    except ValueError:
        print("AssertionError: the arguments are bad")
        return 1
    words = s.split()
    res = [a for a in words if (lambda x: x > n)(len(a))]

    print(res)


if __name__ == "__main__":
    main()
