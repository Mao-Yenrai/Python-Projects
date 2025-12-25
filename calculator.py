# Simple Command-Line Calculator in Python
#
# This program implements a basic calculator that runs in the terminal.
# It supports the following operations:
# - Addition (+)
# - Subtraction (-)
# - Multiplication (*)
# - Division (/)
# - Exponentiation (^)
#
# Features:
# - Accepts floating-point numbers for calculations
# - Includes error handling for invalid inputs (non-numeric values)
# - Prevents division by zero
# - Validates operation symbols
# - Continues running until the user chooses to exit
# - Prompts user confirmation before each calculation continuation
#
# Usage:
# 1. Run the script
# 2. Enter the first number when prompted
# 3. Enter the operation symbol (+, -, *, /, ^)
# 4. Enter the second number
# 5. View the result
# 6. Choose to continue (yes) or exit (no)

print("Hello, I am your personal calculator. Let's get started!")

while True:
    try:
        print("Enter the first number...")
        first = float(input())

        print("Enter the operation symbol: +, -, *, /, ^")
        operation = input()

        print("Enter the second number...")
        second = float(input())

        if operation == '+':
            result = first + second
        elif operation == '-':
            result = first - second
        elif operation == '*':
            result = first * second
        elif operation == '/':
            if second == 0:
                print("Error: division by zero!")
                continue
            result = first / second
        elif operation == '^':
            result = first ** second
        else:
            print("Invalid operation!")
            continue

        print(f"Result: {result}")

        while True:
            print("Do you want to continue? (yes/no)")
            cont = input().lower()
            if cont == 'yes':
                break
            elif cont == 'no':
                print("Goodbye!")
                exit()
            else:
                print("I didn't understand, please write yes or no")

    except ValueError:
        print("Error: enter a number!")
