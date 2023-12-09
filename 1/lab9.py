import re


def main():
    print(task1("hello123"))
    print(task1("helLo123"))
    print(task2("Hello123!"))
    print(task2("hello123!"))
    print(task3("192.168.25.100"))
    print(task3("192.168.256.100"))
    print(task4("12:34:56"))
    print(task4("12:34:61"))
    print(task4("24:34:61"))
    print(task5("12345-6789"))
    print(task5("12345"))
    print(task5("12d345"))
    print(task6("john_doe-123"))
    print(task6("john_doE-123"))
    print(task6("john"))
    print(task7("7512-345656-51234"))
    print(task7("6512-3456-5234"))
    print(task7("5512-345656-51234"))
    print(task10("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))
    print(task10("fe80:2030:31:24"))

    return


def task1(text):
    pattern = "^[a-z0-9]+$"
    return bool(re.match(pattern, text))


def task2(text):
    pattern = "(?=[A-Z])"
    return bool(re.match(pattern, text))


def task3(text):
    pattern = "^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2})(\\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2})){3}$"
    return bool(re.match(pattern, text))


def task4(text):
    pattern = "^([01]?[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$"
    return bool(re.match(pattern, text))


def task5(text):
    pattern = "^[0-9]{5}-[0-9]{4}$|^[0-9]{5}$"
    return bool(re.match(pattern, text))


def task6(text):
    pattern = "^[a-z0-9_-]{6,12}$"
    return bool(re.match(pattern, text))


def task7(text):
    pattern = "^[4-6]\\d{3}-\\d{4}-\\d{4}-\\d{4}|[4-6]\\d{3}-\\d{6}-\\d{5}$"
    return bool(re.match(pattern, text))


def task8(text):
    pattern = "^[0-9]{3}-[0-9]{2}-[0-9]{4}$"
    return bool(re.match(pattern, text))


def task9(text):
    pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@#$%])[A-Za-z\\d@#$%]{8,}$"
    return bool(re.match(pattern, text))


def task10(text):
    pattern = "^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"
    return bool(re.match(pattern, text))


main()
