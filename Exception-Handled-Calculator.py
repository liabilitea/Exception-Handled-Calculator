# Import modules for UI
import tkinter as tk
from tkinter import messagebox
# Define Calculator class to manage and customize the code easier
class Calculator:
    def __init__(self, ui):
        # Initialize UI
        self.ui = ui
        ui.title("Calculator")
        ui.geometry("300x350")
        ui.configure(bg='#ffcccc')
    
        # Create labels for operation and operation options 
        self.operation_label = tk.Label(ui, text="Choose an operation:", bg='#ffcccc')
        self.operation_label.pack(pady=10)

        self.operation_var = tk.StringVar(ui)
        self.operation_menu = tk.OptionMenu(ui, self.operation_var, "+", "-", "*", "/")
        self.operation_menu.pack(pady=10)

        # Create labels and fields for numbers 
        # Number1
        self.num1_label = tk.Label(ui, text="Enter first number:", bg='#ffcccc')
        self.num1_label.pack(pady=10)
        
        self.num1_entry = tk.Entry(ui)
        self.num1_entry.pack(pady=10)
        # Number2
        self.num2_label = tk.Label(ui, text="Enter second number:", bg='#ffcccc')
        self.num2_label.pack(pady=10)
        
        self.num2_entry = tk.Entry(ui)
        self.num2_entry.pack(pady=10)

        #Create label for result
        self.result_label = tk.Label(ui, text="", bg='#ffcccc')
        self.result_label.pack(pady=10)

        #Create calculate button
        self.calculate_button = tk.Button(ui, text="Calculate", command=self.calculate)
        self.calculate_button.pack(pady=10)



# WAG MUNA GALAWIN T.T
#Define calculate method 
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
