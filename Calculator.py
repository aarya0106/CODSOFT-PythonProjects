while True:
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    print(" 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division\n 5. Quit\n  ")
    choice = int(input("Enter the Choice: "))
    if choice == 1:
        result = num1 + num2
    elif choice == 2:
        result = num1 - num2
    elif choice == 3:
        result = num1 * num2
    elif choice == 4:
        result = num1 / num2
    elif choice == 5:
        break
    else:
        print("Invalid Input")

    print(f"Result: {result}")