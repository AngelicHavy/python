# Створення екземпляра класу:

class MyClass:
    pass

obj = MyClass()
print(type(obj))  # <class '__main__.MyClass'>
print(type(MyClass))  # <class 'type'>

AnotherClass = MyClass
print(type(AnotherClass))
print(isinstance(obj, AnotherClass))  # True

# Атрибути класу:

class MyClass:
    int_field = 8
    str_field = 'a string'

print(MyClass.int_field)
print(MyClass.str_field)

object1 = MyClass()
object2 = MyClass()

print(object1.int_field)
print(object2.str_field)

MyClass.int_field = 10
print(MyClass.int_field)
print(object1.int_field)
print(object2.int_field)

# Атрибути-дані:

class Person:
    pass

alex = Person()
alex.name = 'Alex'
alex.age = 18

john = Person()
john.name = 'John'
john.age = 20

print(alex.name, 'is', alex.age)
print(john.name, 'is', john.age)

# Методи класу:

class Person:
    def print_info(self):
        print(self.name, 'is', self.age)

alex = Person()
alex.name = 'Alex'
alex.age = 18

john = Person()
john.name = 'John'
john.age = 20

Person.print_info(alex)
Person.print_info(john)

print(type(Person.print_info))
print(type(alex.print_info))

alex.print_info()
john.print_info()

# Клас з конструктором та методами:

class Building:
    def __init__(self, w, c, n=0):
        self.what = w
        self.color = c
        self.numbers = n
        self.mwhere(n)

    def mwhere(self, n):
        # Метод для визначення розташування
        # на основі кількості чисел
        if n <= 0:
            self.where = "відсутні"
        elif 0 < n < 100:
            self.where = "малий склад"
        else:
            self.where = "основний склад"

    def plus(self, p):
        # Метод для додавання чисел
        self.numbers = self.numbers + p
        self.mwhere(self.numbers)

    def minus(self, m):
        # Метод для віднімання чисел
        self.numbers = self.numbers - m
        self.mwhere(self.numbers)

m1 = Building("дошки", "білі", 50)
m2 = Building("дошки", "коричневі", 300)
m3 = Building("цегла", "біла")

print(m1.what, m1.color, m1.where)
print(m2.what, m2.color, m2.where)
print(m3.what, m3.color, m3.where)

m1.plus(500)
print(m1.numbers, m1.where)
