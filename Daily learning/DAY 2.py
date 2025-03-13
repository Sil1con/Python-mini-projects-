# DAY 2

## Task 1 (The division of the number on two digits and their sum )
# two_digit_number = input()
# num1 = int(two_digit_number[0])
# num2 = int(two_digit_number[1])
# sum = num1 + num2
# print("Sum is " + str(sum))

# ## Task 2 (BMI calcul)
# print("BMI calculator")
# height = int(input("Write your height in cm: "))/100
# weight = int(input("Write your weight in kilos: "))
# bmi = round(weight/height ** 2, 3)
# print("Your BMI: " + str(bmi))

## Task 3 (Life is short)
# age = int(input("How old are you?\n"))
# age_in_weeks = age * 52
# max_weeks = 90 * 52
# weeks_left = max_weeks - age_in_weeks
# days_left = weeks_left * 7
# print(f"You have {weeks_left} weeks left")
# print(f"You have {days_left} days left")

## Tip calculator
# print("Tip Calculator")
# bill = float(input("What was the total bill?\n"))
# amount_of_people = int(input("How many people will split the bill: "))
# tip = int(input("How much tip would you like to give (in percent)\n %: "))
# amount_of_money = round(bill / amount_of_people * (tip/100 + 1), 3)
# print(f"Each person should pay {amount_of_money}")