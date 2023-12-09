import json


def main():
    # print(task1())
    # print(task2())
    # print(task3())
    # print(task4())
    # print(task5())
    # print(task6())
    # print(task7())
    # print(task8())
    return


def task1():
    resultDict = dict()
    with open("‪C:\\Users\\R\\Desktop\\python\\1\\lab8\\words.txt", "r") as file:
        for line in file:
            cleaned_line = line.strip()
            if cleaned_line not in resultDict:
                resultDict[cleaned_line] = 1
            else:
                resultDict[cleaned_line] += 1
    print(resultDict)
    return sorted(resultDict.items(), key=comparator, reverse=True)[:10]



def task2():
    i = 0
    rowsCount = 0
    columnsCount = 0
    with open("C:\\Users\\R\\Desktop\\python\\1\\lab8\\email.csv", "r") as file:
        for line in file:
            if i == 0:
                columnsCount = len(line.split(";"))
                i += 1
            rowsCount += 1
    return {'columns': columnsCount}, {'rows': rowsCount}


def task3():
    result = ""
    wordToReplace = " a "
    replacer = " goodbye "
    with open("‪C:\\Users\\R\\Desktop\\python\\1\\lab8\\text.txt", "r") as file:
        for line in file:
            result += line.replace(wordToReplace, replacer) + " "
    return result


def comparator(resultDict):
    return resultDict[1]


def task4():
    keysList = list()
    with open("‪C:\\Users\\R\\Desktop\\python\\1\\lab8\\file.json", "r") as file:
        for line in file:
            buff = line.split(":")
            if len(buff) == 2:
                keysList.append(buff[0].strip().replace("\"", ""))
    return keysList


def task5():
    with open("‪C:\\Users\\R\\Desktop\\python\\1\\lab8\\file.json", 'r') as file:
        jsonData = json.load(file)
        result = counter(jsonData)
    print(f"Кількість масивів: {result[1]}, \nКількість об'єктів: {result[0]}.")


def counter(myData):
    objectCount = 0
    arrayCount = 0
    stack = [myData]
    while stack:
        currentData = stack.pop()
        if isinstance(currentData, dict):
            objectCount += 1
            stack.extend(currentData.values())
        elif isinstance(currentData, list):
            arrayCount += 1
            stack.extend(currentData)
    return [objectCount, arrayCount]


def task6():
    filter_key = 'position'
    filter_value = 'Software Engineer'
    destination = "‪C:\\Users\\R\\Desktop\\python\\1\\lab8\\result.txt"
    with open("‪C:\\Users\\R\\Desktop\\python\\1\\lab8\\file.json", 'r') as input_file:
        myData = json.load(input_file)
    result = []
    for value in myData:
        employees = myData[value]
        if isinstance(employees, list):
            for employee in employees:
                if isinstance(employee, dict) and filter_key in employee and employee[filter_key] == filter_value:
                    result.append(employee)

    with open(destination, 'w') as output:
        json.dump(result, output, indent=2)
    print(f"Filtered data saved to {destination}")


main()
