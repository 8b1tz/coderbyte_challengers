from collections import Counter


def loop(list2):
    list1 = []
    for x in list2:
        list1.append(x)
    return list1


def MinWindowSubstring(strArr):
    word = strArr[0]
    mask = strArr[1]
    test = []

    start = 0
    end = 0

    while start != (len(word) - 1):
        result = loop(word[start:end])
        if result:
            counter1 = Counter(mask)
            counter2 = Counter(result)
            sub = counter1 - counter2
            checker = []
            for c, v in sub.items():
                if v <= 0:
                    checker.append(True)
                else:
                    checker.append(False)           
            if all(checker):
                test.append(''.join(result))
        if end != (len(word) - 1):
            end += 1

        elif end == (len(word) - 1) and start != (len(word) - 1):
            start += 1
            end = 0

    return min(test, key=lambda x: len(x))


print(MinWindowSubstring(input()))
