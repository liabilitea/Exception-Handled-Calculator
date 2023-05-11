# Exception-Handled-Calculator
***
## Description

This Python project serves as a simple calculator, which allows users to perform four basic arithmetic operations: addition, subtraction, multiplication, and division. The program uses exception handling to deal with any errors or exceptions that may arise during calculations. In case the user inputs invalid values or tries to divide by zero, the program will catch the error and showcase an error message.

The final code executes the calculation in a GUI, which was made by employing the Tkinter library. However, it can be run in the terminal, where it uses the same algorithm as the GUI execution. The code looks like this (you can also access the code from my previous commit):


  ```
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
    trial = input("Do you want to try again? (Y/N): ")
    if trial.upper() == 'N':
        print("Thank you!")
        break
  ```

## How To Use / Run 

1. Install Python on your computer to run the code. You can download its latest version here: https://www.python.org/downloads/
2. Open an IDE and paste the code.
3. Save the file with a .py extension.
4. Run the code.
5. A Graphical User Interface will appear, select the operation you want to perform from the dropdown menu.
6. Enter the first number in the "Enter first number" field and the second number in the "Enter second number" field.
7. Click the "Calculate" button, then the result will appear in the "Result" field.
8. After clicking the calculate button, a popup window will appear asking if you want to input numbers and operations again.
9. If you select "Yes", the "Result" field will be erased. If you select "No", the GUI will close.
    

## Demo

You can access my demo through this link:

https://drive.google.com/file/d/1EcKxFcVYVAH45Fq9DKIXwv4yd7IadQ15/view?usp=share_link
