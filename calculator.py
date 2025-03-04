# Collaborative Menu-Driven Modular Calculator

# Dictionary to store all operations (extensible by collaborators)
operations = {}

def add_operation(name, func):
    """Register a new operation."""
    operations[name] = func

# Basic Operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def exponentiate(a, b):
    return a ** b

# Register basic operations in the calculator
add_operation("1. Add", add)
add_operation("2. Subtract", subtract)
add_operation("3. Multiply", multiply)
add_operation("4. Divide", divide)
add_operation("5. Exponentiate", exponentiate)

def show_menu():
    """Display the menu options."""
    print("\n=== Modular Calculator Menu ===")
    for op in operations:
        print(op)
    print("6. Exit")

def calculator():
    print("Welcome to the Collaborative Modular Calculator!")

    while True:
        show_menu()
        choice = input("Choose an operation (1-6): ").strip()

        if choice == "6":
            print("Exiting calculator. Goodbye!")
            break

        operation_key = {
            "1": "1. Add",
            "2": "2. Subtract",
            "3": "3. Multiply",
            "4": "4. Divide",
            "5": "5. Exponentiate"
        }.get(choice)

        if operation_key not in operations:
            print("Invalid choice, please try again.")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = operations[operation_key](a, b)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    calculator()
