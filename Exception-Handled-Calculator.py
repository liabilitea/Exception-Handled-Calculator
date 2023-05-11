# Create loop to repeat calculations and input writing
while True:
    try:
        # Ask user to choose operatio
        operation = input("Choose an operation (+, -, *, /): ")
        # Ask user to input two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        # Perform the calculation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            else:
                result = num1 / num2
        else:
            raise ValueError("Invalid operation selected.")
        # Display the result of the calculation after raising errors
        print("Result:", result)
    # Handle exceptions based on the conditions met during the calculation
    except ValueError as error:
        print("Error:", error)

    except ZeroDivisionError as error:
        print("Error:", error)
# Ask user if they want to try again or exit the program