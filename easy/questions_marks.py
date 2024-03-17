def QuestionsMarks(strParam):
    save = 0
    sum = 0
    for x in strParam:
        if x.isnumeric():
            sum += int(x)
        elif x == '?':
            if sum == 0:
                save = 0
            else:
                save += 1
        elif (save == 3) and (sum == 10):
            return True
    return False
