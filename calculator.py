def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero is not allowed"

def calculator():
    print("Welcome to the calculator!")
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice (1/2/3/4): ")
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))

    if choice == "1":
        result = add(num1, num2)
        print("The result is:", result)
    elif choice == "2":
        result = subtract(num1, num2)
        print("The result is:", result)
    elif choice == "3":
        result = multiply(num1, num2)
        print("The result is:", result)
    elif choice == "4":
        result = divide(num1, num2)
        print("The result is:", result)
    else:
        print("Invalid choice. Please try again.")

# Call the calculator function to start the program
calculator()
