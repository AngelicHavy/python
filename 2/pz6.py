# Використання рядків:
# A

s1 = "Рядок 1"
s2 = 'Рядок 2'
print(s1, s2)

s3 = str(8)
print(s3)

s4 = """ Lesson2. Variables and Data Types
Some data types explained in this lesson:
- int, - bool, - float, - complex, - str """
print(s4)

s5 = "started\
continued"
print(s5)

# Б

string = "a string"
print(string[0])    # 'a'
print(string[2])    # 's'
print(string[-1])   # 'g'

# В

string = "a string"
print(string[2:5])   # 'str'
print(string[:5])    # 'a str'
print(string[2:])    # 'string'
print(string[::2])   # 'asrn'

print(string[2] + string[-3:])  # 'sing'


# Г

string = input('Введіть рядок: ')
if 'q' in string:
    print('В цьому рядку є символ "q"')
else:
    print('В цьому рядку немає символу "q"')

# Д

string = input('Введіть рядок: ')
print('Довжина цього рядка:', len(string))

#Приклади операцій над рядками:

str1 = 'hel'
str2 = 'lo'
result = str1 + str2
print(result)

a = 48
b = 73
message1 = '%d + %d = %d' % (a, b, a + b)
print(message1)

message2 = '{} - {} = {}'.format(a, b, a - b)
print(message2)

s = 'Hello, World!'
print(s[0])         # 'H'
print(s[4])         # 'o'
print(s[-1])        # '!'
print(s[2:7])       # 'llo, '
print(s[2:7:2])     # 'lo'

#Виведення рядків чисел за вказаною комбінацією:

try:
    N = int(input('Введіть N = '))
except Exception:
    print('Введіть число!!!')
else:
    M = N
    pp = ''
    while M != 0:
        i = M
        L = []
        while i != 0:
            if i <= M:
                L.append(str(i))
                i -= 1
        a = list(L)
        pp = ''.join(a)
        print(pp)
        M = M - 1

#Середнє арифметичне послідовності:

from math import *

a = input('Input first number: ')
if not a.isdigit():
    print("String value can not be entered or number is negative, restart the program!")
    exit()
else:
    a = int(a)

if a == 0:
    print("The number can not be zero")
    input()

count = 0
ar = 0

while True:
    ar += a
    count += 1
    try:
        a = int(input('Input next number or Enter 0 to finish: '))
    except:
        print("String value can not be entered or number is negative, restart the program!")
        exit()
    else:
        if a == 0:
            break

ar = ar / count
print("Average: ", ar)
