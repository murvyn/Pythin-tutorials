# from abc import ABC, abstractmethod
from collections import namedtuple
# import math
# from collections import deque
# from array import array
# from sys import getsizeof
# from pprint import pprint
# print("Hello world 😂")
# print("*" * 10)

# naming variables
# student_count = 1000
# rating = 4.99
# is_Published = True
# course_name = "Python Programming"

# strings
# use """ """ for long strings
# course = "Python Programming"
# print(len(course))
# print(course[0])
# print(course[-1])
# print(course[0:3])

# numbers
# x = 1v
# x = 1.1
# x = 1 + 2j

# working with numbers
# print(round(2.9))
# print(abs(-2.9))
# print(math.ceil(2.2))

# input
# x = input("x: ")
# y = int(x) + 1
# print(f"x: {x}, y: {y}")

# conditional statements
# temperature = 35
# if temperature > 30:
#     print("It's warm")
#     print("Drink water")
# elif temperature > 20:
#     print("It's nice")
# else:
#     print("It's cold")
# print("done")

# ternary operator
# age = 22
# message = "Eligible" if age >= 18 else "Not Eligible"
# print(message)

# logical operators
# high_income = False
# good_credit = True
# student = False

# if (high_income or good_credit) and not student:
#     print("Eligible")
# else:
#     print("Not eligible")

# chaning comparism operators
# age = 22
# if age >= 18 and age < 65:
#     if 18 <= age < 65:
#         print("Eligible")

# for loop
# for number in range(1, 10, 2):
#     print("Attempt", number, number * ".")
# successful = True
# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break
# else:
#     print("Attempted 3 times")
# for number in range(5):
#     for number1 in range(3):
#         print(f"{number}, {number1}")

# while loop
# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)

# functions
# def mutiply(*numbers):
#     print(numbers)


# def save_def(**user):
#     print(user)

# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print("Start")
# print(multiply(1, 2, 3, 4))

# fizzbuzz
# def fizz_buzz(input):
#     if input % 5 == 0 and input % 3 == 0:
#         return "FizzBuzz"
#     elif input % 3 == 0:
#         return "Fizz"
#     elif input % 5 == 0:
#         return "Buzz"
#     else:
#         return input

# print(fizz_buzz(1))

# DATA STRUCTURES
# lists
# letters = ["a", "b", "c"]
# matrix = [[0,1], [2,3]]
# zeros = [0] * 5
# combined = zeros + letters
# numbers = list(range(20))
# chars = list("Hello World")
# print(len(chars))

# numbers  = list(range(20))
# print(numbers[::2])

# list unpacking
# numbers = [1, 2, 3]
# first, second, third = numbers
# first, second, *other  = numbers

# looping
# letters = ["a", "b", "c"]
# for index, letter in enumerate(letters):
#     print(index, letter)

# add
# letters.append("d")
# letters.insert(0, "-")

# remove
# letters.pop()
# letters.pop(0)
# letters.remove("d")
# del letters[0:3]
# letters.clear[]

# finding items
# print(letters.count("d"))
# if "d" in letters:
#     print(letters.index("d"))

# sorting
# numbers = [3,51,2,8,6]
# numbers.sort(reverse=True)
# print(sorted(numbers, reverse=True))
# print(numbers)

# items = [
#     ("Product1", 10),
#     ("Product3", 14),
#     ("Product2", 9),
# ]


# def sort_item(item):
#     return item[1]

# lambda function
# items.sort(key=lambda item: item[1])
# print(items)

# map function
# prices = list(map(lambda item: item[1], items))
# print(prices)

# filter function
# filtered = list(filter(lambda item: item[1] >= 10, items))
# print(filtered)

# list conprehension
# prices = [item[1] for item in items]
# filtered = [item for item in items if item[1] >= 10]

# zip function
# list1 = [1,2,3]
# list2 = [10,20,30]
# print(list(zip("abc", list1, list2)))

# stacks
# browsing_session = []
# browsing_session.append(1)
# browsing_session.pop()
# if not browsing_session:
#     browsing_session[-1]

# queue
# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.popleft()
# print(queue)

# tuple
# point = (1, 2, 3)
# converting list to tuple
# points = tuple(['hello'])
# print(point[0:2])
# x, y, x = point
# if 10 in point:
#     print("exists")

# swapping variables
# x=10
# y=11
# z=x
# x=y
# y=z
# print(x,y)

# or

# x, y = y, x


# array
# numbers = array("i", [1,2,3])

# sets
# numbers = [1, 1, 2, 3, 4]
# first = set(numbers)
# second = {1, 5}
# print(first | second)
# print(first & second)
# print(first - second)
# print(first ^ second)

# dictionaries
# point = {"x": 1, "y": 2}
# point = dict(x=1, y=2)
# point["x"] = 10
# point["z"] = 20
# if "a" in point:
#     print(point["a"])
# or
# print(point.get("a", 0))
# del point["x"]
# print(point)
# for key, value in point.items():
#     print(key, value)

# dic = {x: x * 2 for x in range(5)}
# values = [ x * 2 for x in range(5)]
# sets = {x * 2 for x in range(5)}
# print(values)

# generator
# values = (x * 2 for x in range(100000))
# print(getsizeof(values))

# unpacking operator
# first = [1,2]
# second = [3]
# values = [*first, *second, *"hello"]
# print(values)

# first = {"x": 1}
# second = {"x" : 10, "y": 2}
# combined = {**first, **second, "z": 1}
# print(combined)


# exercise
sentence = "This is a common interview question"
# char_frequency = {}
# for char in sentence:
#     if char in char_frequency:
#         char_frequency[char] += 1
#     else:
#         char_frequency[char] = 1

# char_frequency_sorted = sorted(
#     char_frequency.items(), key=lambda kv: kv[1], reverse=True)
# print(char_frequency_sorted[0])


# exceptions
# try:
# with open("app.py") as file:
# print("File opened")
# age = int(input("Age: "))
# xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
# print("You didn't enter a valid age")
# else:
# print("no exceptions were thrown")
# finally:
#     file.close()
# print("Exception continues")

# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError("Age cannot be 0 or less.")
#     return 10 /age

# try:
#     calculate_xfactor(-1)
# except ValueError as error:
#     print(error)

# classes
# class Point:
#     # constructor
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     # magic methods
#     def __call__(self):
#         return f"({self.x}, {self.y})"

#     # addition
#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)

#     # classmethod
#     @classmethod
#     def zero(cls):
#         return cls(0, 0)

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")


# point = Point.zero()
# point.draw()

# custom containers
# class TagCloud:
#     def __init__(self):
#         self.__tags = {}

#     def add(self, tag):
#         self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

#     def __getitem__(self, tag):
#         return self.__tags.get(tag.lower(), 0)

#     def __setitem__(self, tag, value):
#         self.__tags[tag.lower()] = value

#     def __len__(self):
#         return len(self.__tags)

#     def __iter__(self):
#         return iter(self.__tags)

# cloud = TagCloud()
# cloud.add("python")
# cloud.add("python")
# cloud.add("python")
# cloud["chem"] = 10
# len(cloud)
# print(cloud.__dict__)

# property
# class Projuct:
#     def __init__(self, price):
#         self.price = price

#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def price(self, value):
#         if value < 0:
#             raise ValueError("Price cannot be negative")
#         self.__price = value


# inheritance / method overriding
# class Animal:
#     def __init__(self):
#         print("Animal constructor")
#         self.age = 1

#     def eat(self):
#         print("eat")


# class Mammal(Animal):
#     def __init__(self):
#         print("Mammal constructor")
#         self.weight = 5
#         super().__init__()

#     def walk(self):
#         print("walk")


# class Fish(Animal):
#     def swim(self):
#         print("swim")

# multiple inheritance
# class Flyer:
#     def fly(self):
#        pass


# class Swimmer:
#     def swim(self):
#         pass


# class FlyingFish(Flyer, Swimmer):
#     pass


# good example of inheritance
# class InvalidOperationError(Exception):
#     pass


# class Stream(ABC):
#     def __init__(self):
#         self.opened = False

#     def open(self):
#         if self.opened:
#             raise InvalidOperationError("Stream already opened")
#         self.opened = True

#     def close(self):
#         if not self.opened:
#             raise InvalidOperationError("Stream already closed")
#         self.opened = False

#     @abstractmethod
#     def read(self):
#         pass


# class FileStream(Stream):
#     def read(self):
#         print("reading data from a file")


# class NetworkStream(Stream):
#     def read(self):
#         print("reading data from a network")

# stream = Stream()
# stream.open()


# polymorphism
# class UIControl(ABC):
#     def draw(self):
#         pass

# class TextBox(UIControl):
#     def draw(self):
#         print("TextBox")

# class DropDownList(UIControl):
#     def draw(self):
#         print("DropDownList")

# def draw(controls):
#     for control in controls:
#         control.draw()

# extending built-in types
# class Text(str):
#     def duplicated(self):
#         return self + self


# class TrackableList(list):
#     def append(self, object):
#         print("Append called")
#         super().append(object)


# data classes
Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
print(p1 == p2)
