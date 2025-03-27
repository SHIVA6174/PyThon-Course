# Creating a Custom Exception Class:
class AgeTooSmallError(Exception):
    """Exception raised for age below the required limit."""

    def __init__(self, message="Age must be at least 18!"):
        self.message = message
        super().__init__(self.message)


#  Raising a Custom Exception:

age = int(input("Enter your age: "))
if age < 18:
    raise AgeTooSmallError("You must be at least 18 years old!")
else:
    print("Access granted.")


# Handling a Custom Exception:
try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise AgeTooSmallError
    print("Access granted.")
except AgeTooSmallError as e:
    print("Error:", e)
