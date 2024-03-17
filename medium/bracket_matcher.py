def loop(lst):
    for i, x in enumerate(lst):
        if x == '(':
            closing_index = lst.index(')')
            if closing_index > i:
                lst.pop(i)
                lst.pop(closing_index - 1)
            return lst
    return None


def BracketMatcher(strParam):
    test = [x for x in strParam if x in ['(', ')']]

    while True:
        test = loop(test)
        if not test: 
            break
        if len(test) % 2 != 0:
            return 0
    return 1
