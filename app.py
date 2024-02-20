# import math
# from collections import deque
# from array import array
# from sys import getsizeof
from pprint import pprint
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
# sentence = "This is a common interview question"
# char_frequency = {}
# for char in sentence:
#     if char in char_frequency:
#         char_frequency[char] += 1
#     else:
#         char_frequency[char] = 1

# char_frequency_sorted = sorted(
#     char_frequency.items(), key=lambda kv: kv[1], reverse=True)
# print(char_frequency_sorted[0])
