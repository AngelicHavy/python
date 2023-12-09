#task0
def task0():
    return 4

result = task0()
print(result) 

#task1
def task1(input_string):
    length = len(input_string)
    return length

input_str = "Hello,world!"
result = task1(input_str)
print("Довжина рядка:", result)

#task2
def task2(number1, operator, number2):
    if operator == "+":
        result = number1 + number2
    elif operator == "-":
        result = number1 - number2
    elif operator == "/":
        result = number1 / number2
    elif operator == "//":
        result = number1 // number2
    elif operator == "**":
        result = number1 ** number2
    elif operator == "*":
        result = number1 * number2
    else:
        result = None 
    
    return result

num1 = 5
op = "+"
num2 = 23
result = task2(num1, op, num2)
print(f"{num1} {op} {num2} = {result}")

#task3
def task3(number_list):
    if not number_list:
        return None

    max_number = number_list[0] 
    for number in number_list:
        if number > max_number:
            max_number = number

    return max_number

numbers = [12, 3, 2, 11]
result = task3(numbers)
print("Максимальне число:", result)