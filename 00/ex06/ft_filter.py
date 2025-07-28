def _isTrue(o: any) -> bool:
    if o:
        return True
    return False


def ft_filter(f: callable(any), obj: any) -> iter:
    """
    Return an iterator yielding those items of iterable
    for which function(item) is true.
    If function is None, return the items that are true.
    """
    if not f:
        f = _isTrue
    return iter([i for i in obj if f(i)])


def main():
    """
    test for ft_filter,
    """
    case1 = [38, 4, 2, 1, -3, 0, 0, 1, 2]
    case2 = {'name': 'jane', 'familyname': 'doe', 'age': 0, 'result': None}
    case3 = (0, None, float("nan"), 1, 8.3, "hundred")
    case4 = {1, 0, 7, 9, 3, 4}
    cases = {'list': case1, 'dict': case2, 'set': case3, 'tuple': case4}
    for case in cases:
        ft_it = ft_filter(None, cases[case])
        it = filter(None, cases[case])
        print(f"test : {case} ----------------------")
        print(f"{cases[case]}")
        print("filter result: ")
        while True:
            try:
                print(it.__next__(), end=" ")
            except StopIteration:
                break
        print("\nft_filter result: ")
        while True:
            try:
                print(ft_it.__next__(), end=" ")
            except StopIteration:
                break
        print("\n")


if __name__ == "__main__":
    main()
