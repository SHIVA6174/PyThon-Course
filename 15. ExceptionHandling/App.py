"""
🔹 What is Exception Handling?
An exception is an error that disrupts the normal flow of a program.
Python provides a way to handle these exceptions gracefully using try-except blocks.

👉 The try block contains the code that might cause an error.
👉 The except block catches the error and handles it instead of crashing the program.
👉 The finally block always runs, whether an exception occurs or not.
👉 The else block executes only if there’s no exception in try.

"""

# without exception handling:

print("connection established........")
num1: int = int(input("Enter a Num1: "))  # 100
num2: int = int(input("Enter a Num2: "))  # 0
print(num1 // num2)  # ZeroDivisionError: integer division or modulo by zero
print("connection is terminated!")

# With exception handling:

try:
    print("connection established........")
    num1: int = int(input("Enter a Num1: "))  # 100
    num2: int = int(input("Enter a Num2: "))  # 0
    print(num1 // num2)  # ZeroDivisionError: integer division or modulo by zero
except ZeroDivisionError as e:
    print(e)
finally:  # Always Executes
    print("connection is terminated!")


# 🔹 Catching Multiple Exceptions: 👉 Handles multiple errors separately based on the type of exception.

try:
    num1: int = int(input("Enter a Num1: "))  # 100
    num2: int = int(input("Enter a Num2: "))  # shiva
    print(num1 // num2)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")


# 🔹 Using else (Runs if No Error)

try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input!")
else:
    print("No errors occurred!")


#  Raising Exceptions Manually (raise)

try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise ValueError("You must be 18 or older!")
    else:
        print("Welcome To Our Advantures World!")
except ValueError as e:
    print(e)

# 🔥 Summary:

# Use try to run risky code.
# Use except to catch errors.
# Use finally to run cleanup code (always executes).
# Use else to execute code when no exception occurs.
# Use raise to manually trigger exceptions.
