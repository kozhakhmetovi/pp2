# ex1
"""
Define a class which has at least two methods: getString:
to get a string from console input printString: to print the string in upper case.
"""
class StringInputAndOutput:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Введите строку: ")

    def printString(self):
        print("Строка в верхнем регистре:", self.input_string.upper())


string = StringInputAndOutput()
string.getString()
string.printString()

# ex2
"""
Define a class named Shape and its subclass Square. 
The Square class has an init function which takes a length as argument. 
Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
"""


class Shape:
    def __init__(self, length=0):
        self.length = length

    def area(self):
        return self.length


class Square(Shape):
    def __init__(self, length=0):
        super().__init__(length)

    def area(self):
        return self.length * self.length


shape = Shape(5)
print("shape:", shape.area())

square = Square(4)
print("square:", square.area())
# ex3
"""
Define a class named Rectangle which inherits from Shape class from task 2. 
Class instance can be constructed by a length and width. 
The Rectangle class has a method which can compute the area.
"""


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length


rectangl = Rectangle(4, 5)
print('rectangle: ', rectangl.area())

# ex4
"""
Write the definition of a Point class. Objects from this class should have a

a method show to display the coordinates of the point
a method move to change these coordinates
a method dist that computes the distance between 2 points

"""
import math


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f'x={self.x}  y={self.y}')

    def move(self, newx, newy):
        self.x = newx
        self.y = newy

    def dist(self, other_point):
        return math.sqrt((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2)


p1 = Point(2, 4)
p2 = Point(6, 8)

p1.show()
p2.show()

p1.move(3, 6)
p1.show()

print(f'dist: {p1.dist(p2)}')

# ex5
"""
Create a bank account class that has attributes owner, 
balance and two methods deposit and withdraw. 
Withdrawals may not exceed the available balance. 
Instantiate your class, make several deposits and withdrawals, 
and test to make sure the account can't be overdrawn.

class Account:
    pass
"""


class Bank:
    def __init__(self, money):
        self.balanc = money

    def balance(self):
        print(f'balance: {self.balanc}')

    def deposit(self, dep):
        self.balanc += dep
        print(f'deposit of {dep} successfully made. New balance: {self.balanc}')

    def withdraw(self, wit):
        if self.balanc < wit:
            print('insufficient funds!')

        else:
            self.balanc -= wit
            print(f'withdrawal of {wit} successfully made. New balance: {self.balanc}')


user = Bank(1000)

user.balance()
user.deposit(100)
user.balance()
user.withdraw(1200)
user.withdraw(1000)

# ex6
"""
Write a program which can filter prime numbers in a list by using filter function. 
Note: Use lambda to define anonymous functions.
"""
class PrimeFilter:
    def __init__(self, numbers):
        self.numbers = numbers

    def is_prime(self, n):
        if n < 2:
            return True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return True
        return False

    def filter_primes(self):
        return list(filter(lambda x: self.is_prime(x), self.numbers))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_filter = PrimeFilter(numbers)
prime_numbers = prime_filter.filter_primes()

print("Prime numbers:", prime_numbers)
