# Визначення функції hello_world

def hello_world():
    print('Hello, World!')

# Виклик функції
hello_world()

# Формальний параметр функції:

def print_numbers(limit):
    for i in range(limit):
        print(i)

# Виклик функції print_numbers, її формальний
# параметр limit замінюють фактичним параметром 10
print_numbers(10)

# Виклик функції print_numbers з фактичним параметром n

def print_numbers(limit):
    for i in range(limit):
        print(i)

# Виклик функції з фактичним параметром n
n = int(input('Введіть n: '))
print_numbers(n)

# Виклик функції main

def print_numbers(limit):
    for i in range(limit):
        print(i)

def main():
    n = int(input('Введіть n: '))
    print_numbers(n)

# Виклик функції main
main()

# Визначення функції add_numbers та її виклик:

def add_numbers(a, b):
    return a + b  # вихід функції - сума параметрів

# Виклик функції
x = add_numbers(2, 3)
print(x)

# Використання **kwargs для передачі іменованих параметрів:

def function(**kwargs):
    print(kwargs)

function(arg1='value1', arg2='value2')

# Можна розпакувати відображення
# в іменовані параметри при виклику функції
options = {
    'sep': ', ',
    'end': ';\n'
}
print('value1', 'value2', **options)
# Результат: {'arg1': 'value1', 'arg2': 'value2'}

# Виклик функції hello з параметром за замовчуванням:

def hello(name='Alex'):
    print('Hello, ', name, '!', sep='')

# Виклик функції
hello('Python')
hello()
# Якщо параметр не задано, використовується значення за замовчуванням ('Alex')
