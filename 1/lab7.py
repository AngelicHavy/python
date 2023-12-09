def main():
    task1()
    task2()
    task3()
    task4()
    tupleList = [('John', (2, 1, 3)), ('Jane', (4, 3, 5)), ('Jack', (5, 4, 4))]
    print(task5(tupleList))
    return


def task1():
    try:
        print(f"Ваш вік: {int(input('Введіть Ваш вік: '))}")
    except ValueError:
        print("Помилка! Ви ввели не число!")


def task2():
    try:
        num1 = int(input("Введіть перше число: "))
        num2 = int(input("Введіть друге число: "))
        print(f'Добуток: {num1 * num2}')
    except ValueError:
        print("Помилка! Ви ввели не число!")


def task3():
    try:
        string = input("Введіть будь-який рядок: ")
        length = len(string)
        if length < 1:
            raise IOError
        print(f'Довжина рядка: {length}')
    except IOError:
        print("Ви ввели пустий рядок!")


def task4():
    numberList = list()
    while True:
        try:
            num = input("Введіть ціле число: ")
            if num == "":
                if len(numberList) == 0:
                    print("Список чисел пустий!")
                    return
                result = 0
                for numb in numberList:
                    result += numb
                print(result)
                return
            else:
                numberList.append(int(num))
        except ValueError:
            continue


def task5(tupleList):
    resultList = list()
    try:
        for data in tupleList:
            if len(data) != 2:
                raise ValueError
            if not isinstance(data[0], str):
                raise ValueError
            if len(data[1]) < 1:
                raise ValueError
            average = 0
            for mark in data[1]:
                if not isinstance(mark, int):
                    raise ValueError
                average += mark
            resultList.append((average / len((data[1])), data[0]))
    except ValueError:
        return "Помилка обробки списку!"
    return resultList


main()
