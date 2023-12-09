def main():
    print(task1(4, 5, 1))
    print(task2([8, 2, 3, 0, 7]))
    print(task3([8, 2, 3, -1, 7]))
    print(task4("dcba4321"))
    print(task5(5))
    print(task6(5, 0, 5))
    task7('The quick Brow Fox')
    print(task8([1, 2, 3, 3, 3, 3, 4, 5]))
    print(task9([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    task10(5)
    return


def task1(number1, number2, number3):
    if number1 > number2 > number3:
        return number1
    elif number2 > number1 > number3:
        return number2
    return number3


def task2(someList):
    suma = 0
    for number in someList:
        suma += number
    return suma


def task3(someList):
    if len(someList) == 0: return 0
    result = 1
    for number in someList:
        result *= number
    return result


def task4(someWord):
    result = ''
    for char in someWord[::-1]:
        result += char
    return result


def task5(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * task5(number - 1)


def task6(number, rangeStart, rangeEnd):
    return rangeStart <= number <= rangeEnd


def task7(someString: str):
    lower = 0
    upper = 0
    for char in someString:
        if char.isalpha():
            if char.isupper():
                upper += 1
            else:
                lower += 1
    print(f"No. of Upper case characters: {upper},\nNo. of Lower case Characters: {lower}")


def task8(someList):
    result = list()
    for value in someList:
        if value not in result:
            result.append(value)
    return result


def task9(someList):
    result = list()
    for value in someList:
        if value % 2 == 0:
            result.append(value)
    return result


def task10(numberOfRows):
    for i in range(0, numberOfRows, 1):
        for j in range(0, numberOfRows - i, 1):
            print(" ", end='')
        for j in range(0, i + 1, 1):
            print(f" {task5(i) // (task5(i - j) * task5(j))}", end="")
        print()

main()
