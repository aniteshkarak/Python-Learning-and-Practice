try:
    a = int(input("Enter first integer: "))
    b = int(input("Enter second integer: "))

    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid integers only.")

except Exception as e:
    print("Unexpected error:", e)
