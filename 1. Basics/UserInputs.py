# Input/Output & String Formatting

name = input("Enter your name: ")
print("Hello, " + name + "!")

age = 21
print(f"I am {age} years old.")  # f-string (Best way)
print("I am {} years old.".format(age))  # Using format()
print("I am " + str(age) + " years old.")  # Using concatenation
