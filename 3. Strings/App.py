Client: str = "Vandana Reddy"
print(Client)
print(type(Client))


# String Indexing (Accessing Characters): Each character in a string has an index (position). +ve Indexing starts from 0. & -ve Indexing starts from -1
text = "Python"
# forward or +ve indexing:
print(text[0])  # P (First character)
print(text[3])  # h (Fourth character)d or
# backword or -ve indexing:
print(text[-1])  # n (Last character)
print(text[-3])  # h (Third last character)


#  String Slicing (Extracting Substrings):[start:stop:step]
text = "PythonProgramming"

print(text[0:6])  # Python (Index 0 to 5)
print(text[:6])  # Python (Same as above)
print(text[6:])  # Programming (From index 6 to end)
print(text[::2])  # PtoPormig (Every 2nd char)
print(text[::-1])  # gnimmargorPnohtyP (Reversed string)

# Common String Methods

# Changing Case

text = "hello Python"

print(text.upper())  # HELLO PYTHON
print(text.lower())  # hello python
print(text.title())  # Hello Python
print(text.capitalize())  # Hello python


# Removing Whitespaces

text = "  Hello World  "

print(text.strip())  # "Hello World"  (Removes spaces from both sides)
print(text.lstrip())  # "Hello World  " (Removes from left)
print(text.rstrip())  # "  Hello World" (Removes from right)


#  Finding and Replacing

text = "Python is great"

print(text.find("is"))  # 7 (Returns the index of "is")
print(text.replace("great", "awesome"))  # Python is awesome


# Checking String Content
text = "hello123"

print(text.isalpha())  # False (Contains numbers)
print(text.isdigit())  # False (Contains letters)
print(text.isalnum())  # True (Only letters & numbers)


# Splitting and Joining

text = "apple,banana,grape"

words = text.split(",")  # Converts into list
print(words)  # ['apple', 'banana', 'grape']

new_text = "-".join(words)  # Joins with "-"
print(new_text)  # apple-banana-grape


"""
🎯 Summary
✔ Indexing (text[0]) → Access specific characters.
✔ Slicing (text[start:end:step]) → Extract substrings.

### 📝 Case Conversion
- `upper()` → Converts all characters to uppercase.  
- `lower()` → Converts all characters to lowercase.  
- `title()` → Capitalizes the first letter of each word.  
- `capitalize()` → Capitalizes only the first letter of the string.  
- `swapcase()` → Swaps uppercase to lowercase and vice versa.  

---

### 📌 Checking Content
- `isalpha()` → Returns `True` if all characters are alphabets.  
- `isdigit()` → Returns `True` if all characters are digits.  
- `isalnum()` → Returns `True` if the string contains only letters & numbers.  
- `isspace()` → Returns `True` if the string has only whitespace.  
- `startswith(substring)` → Checks if the string starts with the given substring.  
- `endswith(substring)` → Checks if the string ends with the given substring.  

---

### 🛠 Modifying Strings
- `strip()` → Removes whitespace from both sides.  
- `lstrip()` → Removes whitespace from the left side.  
- `rstrip()` → Removes whitespace from the right side.  
- `replace(old, new)` → Replaces all occurrences of a substring.  

---

### 🔍 Finding & Counting
- `find(substring)` → Returns the first index of the substring, `-1` if not found.  
- `index(substring)` → Like `find()`, but raises an error if not found.  
- `count(substring)` → Counts occurrences of a substring.  

---

### 🔗 Splitting & Joining
- `split(separator)` → Splits the string into a list based on the separator.  
- `rsplit(separator)` → Splits from the right side.  
- `join(iterable)` → Joins elements of an iterable into a string.  

---

### 🎯 Other Methods
- `zfill(width)` → Pads the string with zeros (e.g., `"5".zfill(3) → "005"`).  
- `center(width, char)` → Centers the string, filling with a character.  
- `ljust(width, char)` → Left-aligns the string.  
- `rjust(width, char)` → Right-aligns the string.  

---

### 🔥 Summary
✔ Case Methods → `upper(), lower(), title(), swapcase()`  
✔ Checking Content → `isalpha(), isdigit(), startswith()`  
✔ Modifying → `strip(), replace()`  
✔ Finding → `find(), index(), count()`  
✔ Splitting & Joining → `split(), join()`  
✔ Formatting → `zfill(), center()`  

"""
