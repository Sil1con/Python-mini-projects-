## DAY 4
# import random

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# item = [rock, paper, scissors]
# finish = False

# print("I see you would like to play Rock, Paper, Scissors\n You're welcome!")
# print("What do you choose?\n 0 is for Rock\n 1 is for Paper\n 2 is for Scissors")

# while finish != True:
#     print("\n\nIf you want to stop the game, enter 9")
#     guess = int(input("Choice: "))
#     rand = round(random.random() * 2)
#     if guess == 9:
#         finish = True
#         print("\nGame over\nSee you soon!")
#     elif guess >= len(item) or guess < 0:
#         print("Select a proper option")
#     else:
#         print("You chose: " + item[guess] +"\n"+  "Computer chose: " + item[rand])
#         if item[guess] == item[0] and item[rand] == item[2]:
#             print("You won")
#         elif item[guess] == item[1] and item[rand] == item[0]:
#             print("You won")
#         elif item[guess] == item[2] and item[rand] == item[1]:
#             print("You won")
#         elif item[guess] == item[rand]:
#             print("Game draw")
#         else:
#             print("Computer win")