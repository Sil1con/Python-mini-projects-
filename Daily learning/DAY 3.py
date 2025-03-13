# DAY 3

## Task 1
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?\n"))
# if height < 120:
#     print("You have to grow taller 120 cm before you can ride")
# else:
#     print("You can ride the roallercoaster!")

## Task 2
# num = int(input("Insert the number: "))
# if num % 2 == 0:
#     print("The given number is even")
# else:
#     print("The given number is odd")

## Task 3
# height = int(input("What is your height in cm\n"))
# if height < 120:
#     print("You have to grow taller 120 cm before you can ride")
# else:
#     print("Depending on your age there is the price for a ticket")
#     age = int(input("What is your age: "))
#     if age < 12:
#         print("You should pay $5")
#     elif age <= 18:
#         print("You should pay $7")
#     else:
#         print("You should pay $12")

## BMI 2.0
# print("BMI calculator 2.0")
# weight = float(input("What is your weight in kilos?\n Kilos: "))
# height = float(input("What is your height in cm?\n Height: "))
# bmi = weight / (height/100) ** 2

# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, you are under weight")
# elif 18.5 <= bmi <= 25:
#     print(f"Your BMI is {bmi}, you have a normal weight")
# elif 25 < bmi <= 30:
#     print(f"Your BMI is {bmi}, you are slightly overweight")
# elif 30 < bmi <= 35:
#     print(f"Your BMI is {bmi}, you are obese")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese")

## Leap Year
# year = int(input("Please, enter the year: "))
# if year % 4 != 0:
#     print("Not leap year")
# else:
#     if year % 100 == 0 and year % 400 == 0:
#         print("Leap year")
#     elif year % 100 != 0 and year % 400 != 0:
#         print("Leap yaer")
#     else:
#         print("Not leap year")

## Task 4 (The roallercoaster + a photo)
# height = int(input("What is your height in cm\n"))
# if height < 120:
#     print("You have to grow taller 120 cm before you can ride")
# else:
#     print("Depending on your age there is the price for a ticket")
#     age = int(input("What is your age: "))
#     if age < 12:
#         bill = 5
#         print("Child ticket is 5")
#     elif age <= 18:
#         bill = 7
#         print("Youth ticket is 7")
#     else:
#         bill = 12
#         print("Adult ticket is 7")
#     photo = input("Do you want a photo?\n Yes or No: ").upper()
#     if photo == "YES":
#         bill += 3
#         print(f"You should pay ${bill} totally")
#     else:
#         print(f"You should pay ${bill}")

## Pizza Order
# print("Welcome in Python Pizza")
# size = input("What size pizza do you want?\n S, M, or L: ").upper()
# add_pepperoni = input("Do you want pepperoni?\n Y or N: ").upper()
# extra_cheese = input("Do you want extra cheese?\n Y or N: ").upper()
# small = 15
# medium = 20
# large = 25
# if size == "S":
#   bill = small
#   if add_pepperoni == "Y":
#     bill += 2
#   if extra_cheese == "Y":
#     bill += 1
#   print(f"Your final bill is: ${bill}.")
# elif size == "M" or size == "L":
#   bill = 0
#   if size == "M":
#     bill = medium
#   else:
#     bill = large
#   if add_pepperoni == "Y":
#     bill += 3
#   if extra_cheese == "Y":
#     bill += 1
#   print(f"Your final bill is: ${bill}.")

## Love Calculator
# name1 = input("What is your name?\n").lower()
# name2 = input("What is another name?\n").lower()
# name = name1 + name2
# true = ["t", "r", "u", "e"]
# love = ["l", "o", "v", "e"]
# x = 0
# y = 0
# for i in true:
#     x += name.count(i)
# for i in love:
#     y += name.count(i)
# score = int(str(x) + str(y))
# if score < 10 or score > 90:
#     print(f"Your score is {score}, you go together like coke and mentos.")
# elif 40 <= score <= 50:
#     print(f"Your score is {score}, you are alright together.")
# else:
#     print(f"Your score is {score}.")