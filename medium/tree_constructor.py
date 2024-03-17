from collections import Counter


def TreeConstructor(strArr):
    parents = Counter([string[3] for string in strArr])
    children = Counter([string[1] for string in strArr])

    for count in parents.values():
        if count > 2:
            return False
    for count in children.values():
        if count > 2:
            return False

    for parent, child in zip(parents, children):
        if parent == child:
            return False
    return True
