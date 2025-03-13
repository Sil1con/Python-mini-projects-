# DAY 9

## Work with dictionaries 
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }

# student_grades = {}

# for student in student_scores:
#   grade = student_scores[student]
#   value = ""
#   if 91 <= grade <= 100 or grade > 100:
#     value = "Outstanding"
#   elif 81 <= grade <= 90:
#     value = "Exceeds Expectations"
#   elif 71 <= grade <= 80:
#     value = "Acceptable"
#   elif grade <= 70:
#     value = "Fail"
#   student_grades[student] = value

# print(student_grades)

## Work with dictionaries and lists
# country = input() # Add country name
# visits = int(input()) # Number of visits
# list_of_cities = eval(input()) # create list from formatted string

# travel_log = [
#   {
#     "country": "France",
#     "visits": 12,
#     "cities": ["Paris", "Lille", "Dijon"]
#   },
#   {
#     "country": "Germany",
#     "visits": 5,
#     "cities": ["Berlin", "Hamburg", "Stuttgart"]
#   },
# ]

# def add_new_country(country, visits, list_of_cities):
#   entity = {}
#   entity["country"] = country
#   entity["visits"] = visits
#   entity["cities"] = list_of_cities
#   travel_log.append(entity)

# add_new_country(country, visits, list_of_cities)
# print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
# print(f"My favourite city was {travel_log[2]['cities'][0]}.")

## Auction program
# logo = '''
#                          ___________
#                          \         /
#                           )_______(
#                           |"""""""|_.-._,.---------.,_.-._
#                           |       | | |               | | ''-.
#                           |       |_| |_             _| |_..-'
#                           |_______| '-' `'---------'` '-'
#                           )"""""""(
#                          /_________\\
#                        .-------------.
#                       /_______________\\
# '''

# def find_winner(participants):
#     winner = ""
#     bid = 0
#     for bidder in participants:
#         if bid < participants[bidder]:
#             bid = participants[bidder]
#             print(winner)
#             winner = bidder
#     return winner

# end_auction = False
# participants = {}
# print(logo + "\n")
# print("Welcome to the Secret Auction!")

# while end_auction != True:
#     name = input("What's your name?: ")
#     bid = int(input("What's your bid?: $"))
#     participants[name] = bid

#     repeat = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
#     if repeat == "no":
#         winner = find_winner(participants)
#         print(f"The winner is {winner} with a bid of {participants[winner]}")
#         end_auction = True
#     elif repeat == "yes":
#         continue