# import math
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