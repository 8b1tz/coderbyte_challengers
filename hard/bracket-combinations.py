def factorial(num):
    if num > 0:
        return num * factorial(num - 1)
    return 1


def BracketCombinations(n):
    return int((factorial(n * 2)) / (factorial(n + 1) * (factorial(n))))


print(BracketCombinations(input()))
