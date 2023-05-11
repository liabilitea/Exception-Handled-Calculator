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

#Define calculate method 
    def calculate(self):
        try:
        
            # Get operation and numbers using UI
            operation = self.operation_var.get()
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
        
            # Perform the calculation
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                result = num1 / num2
            else:        
                raise ValueError("Invalid operation selected.")
            
            # Display the result in UI
            self.result_label.config(text="Result: " + str(result))
    
        # Handle exceptions and display in UI
        except ValueError as error:
            self.result_label.config(text="Error: " + str(error))

        except ZeroDivisionError as error:
            self.result_label.config(text="Error: Cannot divide by zero.")

        # Clear operation and number entry fields
        self.operation_var.set("")
        self.num1_entry.delete(0, 'end')
        self.num2_entry.delete(0, 'end')

        # Ask user if they want to try again or exit using messagebox
        trial = tk.messagebox.askquestion("Try again?", "Do you want to try again?")
        # If yes, clear result label and continue
        if trial == 'yes':
            self.result_label.config(text="")
        else:
        # If no, destroy UI and exit
            self.ui.destroy()

# Create root window and Calculator instance
window = tk.Tk()
calculator = Calculator(window) 

# Start the main event loop 
window.mainloop()