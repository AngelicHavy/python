import array
import random
from array import *
from itertools import product


def main():
    # task1()
    # myDict = generateRandom()
    # task2(myDict)
    # arr = array('i', [2, 2, 3, 3, 5, 7, 9, 8, 7])
    # print(task3(arr))
    # myList = array('i', [10, 11, 12, 13, 14, 15, 17, 18, 19, 20])
    # print(f"Missing number in the said array (10-20): {task4(myList)}")
    # myDict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
    #           {"VIII": "S007"}]
    # task5(myDict)
    # myDict = {'1': ['a', 'b'], '2': ['c', 'd'], '3': ['e', 'f']}
    # task6(myDict)
    # myDict = {'key1': [10, 5, 8, 12, 15], 'key2': [20, 18, 25, 21, 23], 'key3': [7, 9, 15, 11, 14]}
    # task7(myDict)
    myListOfDicts = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300},
                     {'item': 'item1', 'amount': 750}, {'item': 'item3', 'amount': 560},
                     {'item': 'item2', 'amount': 205}]
    task8(myListOfDicts)
    return


def task1():
    start = int(input("Введіть перше число: "))
    end = int(input("Введіть друге число: "))
    replacer = 999
    myArray = array('i')
    for i in range(start, end + 1, 1):
        if i % 2 == 0:
            myArray.append(replacer)
        else:
            myArray.append(i)
    print(myArray)


def task2(dictionary: dict):
    genList = dictionary['kitty']
    print(genList)
    result = {genList[len(genList) - 1], genList[0]}
    print(f"Результат: {result}")


def generateRandom():
    start = int(input("Введіть мінімальне рандомне число: "))
    end = int(input("Введіть максимальне рандомне число: "))
    amount = int(input("Введіть кількість елементів: "))
    genList = list()
    for i in range(0, amount, 1):
        genList.append(random.randint(start, end + 1))
    return {'kitty': genList}


def task3(myArray: array):
    newArr = array('i')
    for i in myArray:
        if not contains(newArr, i):
            newArr.append(i)
    return newArr


def contains(myArray: array, number: int):
    for i in myArray:
        if i == number:
            return True
    return False


def task4(myArr):
    if myArr[0] != 10:
        return 10
    previous = myArr[0]
    for i in myArr:
        if i - previous > 1:
            return i - 1
        previous = i
    if myArr[len(myArr) - 1] != 20:
        return 20


def task5(myDict):
    unics = set()
    for dictionary in myDict:
        for value in dictionary.values():
            unics.update({value})
    print(unics)


def task6(myDict):
    values = list(myDict.values())
    list_combinations = []
    joiner(values, [], list_combinations, 0)
    for combination in list_combinations:
        print(combination)




def joiner(values, current_combination, result, index):
    if index == len(values):
        result.append(''.join(current_combination))
        return

    current_key_values = values[index]
    for value in current_key_values:
        joiner(values, current_combination + [value], result, index + 1)


def task7(myDict):
    result = dict()
    for key, values in myDict.items():
        result[key] = sorted(values, reverse=True)[:3]
        print(f"Highest 3 values for key '{key}': {result[key]}")


def task8(listOfDicts):
    resultDict = dict()
    for dictionary in listOfDicts:
        if dictionary['item'] not in resultDict:
            buffDict = {dictionary['item']: dictionary['amount']}
            resultDict.update(buffDict)
        else:
            resultDict[dictionary['item']] += dictionary['amount']
    print(resultDict)


main()
