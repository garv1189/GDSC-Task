import math


def calculate(expression):
    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Division by zero is not allowed."
    except Exception as e:
        return f"Error: {str(e)}"


while True:
    user_input = input("Enter an expression (or 'quit' to exit): ")

    if user_input.lower() == 'quit':
        break

    result = calculate(user_input)
    print("Result:", result)
