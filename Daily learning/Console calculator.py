# DAY 10

# Calculator

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
stop_program = False
stop_calculation = False
while stop_program != True:
    num1 = float(input("What's your first number?: "))
    while stop_calculation == False:
        for symbol in operations:
            print(symbol)
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        output = operations[operation]
        calculated = output(num1, num2)
        
        if operation in operations == False:
            print("Please, select an appropriate operation")
        else: 
            print(f"{num1} {operation} {num2} = {calculated}")
            answer = input(f"Type 'stop' to finish the program\nType 'yes' to continue with calculating {calculated}, or type 'no' to start a new calculation: ").lower()
            if answer == "stop":
                stop_calculation = True
                stop_program = True
            elif answer == "yes":
                num1 = calculated
                continue
            else:
                break