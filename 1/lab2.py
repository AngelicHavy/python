#task0
def task0(number1, number2):
    result = number1 + number2
    return result

number1 = 22
number2 = 2
result = task0(number1, number2)
print("Sum:", result)

#task1
def task1(number1, znak, number2):
    if znak == '>':
        return number1 > number2
    elif znak == '<':
        return number1 < number2
    elif znak == '>=':
        return number1 >= number2
    elif znak == '<=':
        return number1 <= number2
    elif znak == '==':
        return number1 == number2
    elif znak == '!=':
        return number1 != number2
    else:
        raise ValueError("Невірний знак порівняння")

result = task1(8, '!=', 3)
print(result) 

#task2
def task2(text, number):
    return len(text) > number

text1 = "Hello, World!"
number1 = 4
result1 = task2(text1, number1)
print(result1)

text2 = "Python"
number2 = 8
result2 = task2(text2, number2)
print(result2) 

#task3
def task3(number1, number2, number3):
    return number1 == number2 == number3

result1 = task3(6, 6, 6)
print(result1)

result2 = task3(10, 1, 2)
print(result2)