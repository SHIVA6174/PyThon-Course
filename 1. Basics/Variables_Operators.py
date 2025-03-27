# Variables & Data Types:  Variables store data in Python. No need to declare types explicitly!

name = "Vandana"  # String
age = 22  # Integer
score = 99.89  # Float
is_happy = True  # Boolean

print(f"{name} {age} {score} {is_happy}")

# Operators in Python:

# 1. Arthematic
a = 10
b = 3
print(a + b)  # Addition (13)
print(a - b)  # Subtraction (7)
print(a * b)  # Multiplication (30)
print(a / b)  # Division (3.33)
print(a // b)  # Floor Division (3)
print(a % b)  # Modulus (1)
print(a**b)  # Exponentiation (10^3 = 1000)

# Comparison Operators (Return True or False)

print(10 > 5)  # True
print(10 < 5)  # False
print(10 == 10)  # True
print(10 != 5)  # True
print(10 >= 5)  # True
print(10 <= 5)  # False


#  Logical Operators

x = True
y = False

print(x and y)  # False (Both must be True)
print(x or y)  # True (At least one True)
print(not x)  # False (Reverses value)


# Assignment Operators (=)

x = 10  # Simple assignment
x += 5  # Same as x = x + 5 → x = 15
x -= 3  # Same as x = x - 3 → x = 12
x *= 2  # Same as x = x * 2 → x = 24
x /= 4  # Same as x = x / 4 → x = 6.0
x %= 4  # Same as x = x % 4 → x = 2.0
x //= 2  # Same as x = x // 2 → x = 1.0
x **= 3  # Same as x = x ** 3 → x = 1.0


#  Bitwise Operators (Works at Binary Level)

a = 5  # Binary:  0101
b = 3  # Binary:  0011

print(a & b)  # AND → 0101 & 0011 = 0001 (1)
print(a | b)  # OR  → 0101 | 0011 = 0111 (7)
print(a ^ b)  # XOR → 0101 ^ 0011 = 0110 (6)
print(~a)  # NOT → ~0101 = 1010 (-6) (Inverts bits)
print(a << 1)  # Left Shift  (5 * 2^1 = 10)
print(a >> 1)  # Right Shift (5 / 2^1 = 2)


# Membership Operators (in, not in)

fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)  # True
print("grape" not in fruits)  # True

text = "Hello, Python!"
print("Python" in text)  # True


# Identity Operators (is, is not)

a = [1, 2, 3]
b = a  # Both point to the same list

print(a is b)  # True (Same object)
print(a is not b)  # False (Not different objects)

c = [1, 2, 3]
print(a is c)  # False (Different objects with same values)


# 🎯 Summary
# ✔ Assignment (=) → Assign values (+=, -=, *=, etc.).
# ✔ Bitwise (&, |, ^, ~, <<, >>) → Works at binary level.
# ✔ Membership (in, not in) → Check if a value exists in a sequence.
# ✔ Identity (is, is not) → Check if two variables refer to the same object.
