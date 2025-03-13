# DAY 5

## Average height
# print("Data must be written in this way\n150, 149, 148")
# student_heights = input("Your data: ").split(", ")
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])

# total = 0
# amount_of_students = 0

# for x in student_heights:
#   total += x
#   amount_of_students += 1
# average = round(total / amount_of_students)
# print(f"total height = {total}")
# print(f"number of students = {amount_of_students}")
# print(f"average height = {average}")

# ## Sum of even numbers in range
# target = int(input("Your number: "))
# sum = 0
# for x in range(1, target+1):
#   if x % 2 == 0:
#     sum += x
# print(sum)

## FizzBuzz game
# for x in range(1, 101):
#   if x % 3 == 0 and x % 5 == 0:
#     print("FizzBuzz")
#   elif x % 3 == 0:
#     print("Fizz")
#   elif x % 5 == 0:
#     print("Buzz")
#   else:
#     print(x)

## Password Generator
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
# length = nr_letters + nr_symbols + nr_numbers
# password = []
# for x in range(0, length):
#     rand = round(random.random() * 2)
#     if rand == 0:
#         rand = round(random.random() * (len(letters) - 1))
#         password.append(letters[rand])
#     elif rand == 1:
#         rand = round(random.random() * (len(numbers) - 1))
#         password.append(numbers[rand])
#     elif rand == 2:
#         rand = round(random.random() * (len(symbols) - 1))
#         password.append(symbols[rand])
# random.shuffle(password)
# print(password)