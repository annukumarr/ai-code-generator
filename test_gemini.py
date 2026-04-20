
import sys

def add(x: float, y: float) -> float:
    """Adds two numbers and returns their sum."""
    return x + y

def subtract(x: float, y: float) -> float:
    """Subtracts the second number from the first and returns the difference."""
    return x - y

def multiply(x: float, y: float) -> float:
    """Multiplies two numbers and returns their product."""
    return x * y

def divide(x: float, y: float) -> float:
    """
    Divides the first number by the second.
    Raises a ValueError if the divisor (y) is zero.
    """
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def get_numeric_input(prompt_message: str) -> float:
    """
    Prompts the user for numeric input and handles invalid input gracefully.
    Continuously prompts until a valid floating-point number is entered.

    Args:
        prompt_message (str): The message to display to the user.

    Returns:
        float: The valid numeric input provided by the user.
    """
    while True:
        try:
            return float(input(prompt_message))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def display_menu():
    """Displays the main calculator operation menu to the user."""
    print("\n--- Simple Calculator ---")
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("-------------------------")

def get_operator_symbol(choice: str) -> str:
    """
    Helper function to get the string representation of an operator
    based on the user's menu choice.

    Args:
        choice (str): The user's menu choice ('1', '2', '3', '4').

    Returns:
        str: The operator symbol ('+', '-', '*', '/') or an empty string if invalid.
    """
    if choice == '1': return '+'
    if choice == '2': return '-'
    if choice == '3': return '*'
    if choice == '4': return '/'
    return '' # Should not be reached with valid choice handling

def run_calculator():
    """
    Main function to run the calculator application.
    It provides a continuous loop for performing calculations until the user
    chooses to exit. Handles user input, operation selection, and error cases.
    """
    print("Welcome to the Simple Calculator!")

    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3/4/5): ").strip()

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            sys.exit(0) # Exit the program cleanly
        elif choice in ('1', '2', '3', '4'):
            num1 = get_numeric_input("Enter the first number: ")
            num2 = get_numeric_input("Enter the second number: ")

            result = None
            operator_symbol = get_operator_symbol(choice)

            try:
                if choice == '1':
                    result = add(num1, num2)
                elif choice == '2':
                    result = subtract(num1, num2)
                elif choice == '3':
                    result = multiply(num1, num2)
                elif choice == '4':
                    result = divide(num1, num2)

                print(f"Result: {num1} {operator_symbol} {num2} = {result}")
            except ValueError as e:
                # Catch specific errors like division by zero
                print(f"Operation error: {e}")
            except Exception as e:
                # Catch any other unexpected errors during calculation
                print(f"An unexpected error occurred: {e}")
        else:
            print("Invalid choice. Please select a valid option (1, 2, 3, 4, or 5).")

        print("\n" + "="*40 + "\n") # Separator for better readability between operations

# Entry point for the script execution
if __name__ == "__main__":
    run_calculator()
