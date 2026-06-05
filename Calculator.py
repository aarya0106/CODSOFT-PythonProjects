# 1. Welcome message
print("=== BASIC CALCULATOR ===")

# 2. Get inputs from the user
# We use float() so the user can type decimals (like 5.5) instead of just whole numbers
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# 3. Check the operator and perform the math
if operator == "+":
    result = num1 + num2
    print("Result:", result)

elif operator == "-":
    result = num1 - num2
    print("Result:", result)

elif operator == "*":
    result = num1 * num2
    print("Result:", result)

elif operator == "/":
    # Quick check to prevent a crash if dividing by 0
    if num2 == 0:
        print("Error: You cannot divide by zero!")
    else:
        result = num1 / num2
        print("Result:", result)

else:
    print("Invalid operator! Please run the program again and use +, -, *, or /.")