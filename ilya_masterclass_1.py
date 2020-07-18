class MyClass:
    i = 12345

    def f():
        return 'Hello World'
print(MyClass.i)
print(MyClass.f())

# 5:28 two ways to use an attribute reference


x = MyClass()

print(x.i)
print(x.f)

# 6:31 use instantination of class

class Dog:

    breed = 'Pit Bull'

    def __init__(self, name, color):
        self.name = name
        self.color = color
    def methof(self):
        print(f'{self.name} is a good dog')
        name = self.name

lucky = Dog('Lucky', 'black')
snow = Dog('Snow', 'white')

print(lucky.name)
print(snow.name)
print(lucky.color)
print(snow.color)
print(lucky.breed)
print(snow.breed)

print('')

class MyClass1(object):

    is_agree = True
    is_agree: 1
    def __init__(self, x):
        self.x = x

    def my_method(self, y):
        self.x = y

    @staticmethod
    def my_static_method(x, y):
        return x + y

    @classmethod
    def my_class_method(cls):
        cls.is_agree = False
example = MyClass1(10)
print(example.x)
example.my_method(15)
print(example.x)
print(example.my_static_method(10, 20))
print(example.is_agree)
example.my_class_method()
print(example.is_agree)

print('')

class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def set_salary(self, new_salary):
        self._salary = new_salary

    def get_salary(self):
        return self._salary
    def __count_all_year_salary(self):
        return self._salary * 12
    def get_all_year_salary(self):
        return self.__count_all_year_salary()
employee_1 = Employee('John', 10000)
print(employee_1.get_salary())
employee_1.set_salary(100000)
print(employee_1.get_salary())
print(employee_1.get_all_year_salary())
print('')
class BaseClassName:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print(self.name)

class BaseLasteName:
    def __init__(self, last_name):
        self.last_name = last_name

    def hello_world(self):
        print('Hello World')
class DerivedClassName(BaseClassName, BaseLasteName):
    pass


example = DerivedClassName('John')

print(example.name)
example.get_name()
example.hello_world()