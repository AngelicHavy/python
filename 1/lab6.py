def main():
    task1(4, 1)
    task2(1, 2, 3, "Hello", "World", "!")
    task3([-4, 2, 3, -1, 7])
    task4()
    task5()
    task6()
    task7()


def task1(number1, number2):
    result = (number1, number2)
    print(result[0] + result[1])


def task2(number1, number2, number3, string1, string2, string3):
    result = (number1, number2, number3, string1, string2, string3)
    print(len(result))


def task3(someList):
    result = sorted(tuple(someList), reverse=True)
    print(result[0])


def task4():
    result = ({'name': 'Anzhelika', 'age': 19},)
    print(result[0]['name'])


def task5():
    listOfTuples = [(5, 2, 4, 7), (12, 6, 9, 19), (1, 7, 3, 8)]
    buffer_tuple = tuple(listOfTuples)
    buffer_tuple = sorted(buffer_tuple, key=length)
    print(buffer_tuple[-1][-1])


def length(value):
    return value[0]


def task6():
    listTuple = [(1, 2, 3, 4, 5),
                 (7, 8, 9, 10, 11),
                 (13, 14, 15, 16, 17),
                 (19, 20, 21, 22, 23),
                 (25, 26, 27, 28, 29)]
    product = 1
    for tupleInList in listTuple:
        for number in tupleInList:
            if number % 2 == 0:
                product *= number
    print(product)


def task7():
    tupleOfTuples = ((1, 2), (3, 4), (7, 8), (11, 16), (9, 5))
    result = 0
    for tup in tupleOfTuples:
        result += tup[1]
    print(result)


main()
