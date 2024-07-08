def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def power(x, y):
    return x ** y

def main():
    print("Select operation:")
    print("Add: +")
    print("Subtract: -")
    print("Multiply: *")
    print("Divide: /")
    print("Power: ^")

    while True:
        choice = input("Enter choice: [+, -, *, /, ^]")

        if choice in ['+', '-', '*', '/', '^']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numerical values.")
                continue
        
            if choice == '+':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            
            elif choice == '-':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            
            elif choice == '*':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            
            elif choice == '/':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            
            elif choice == '^':
                print(f"{num1} ^ {num2} = {power(num1, num2)}")
        else:
            print("Invalid input. Please enter a valid option.")

            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

if __name__ == "__main__":
    main()