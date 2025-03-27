"""
📂 What is File Handling?
File handling allows us to read, write, append, and manage files.
It helps us store and retrieve data permanently instead of keeping it only in memory.

1. open(filename, mode)  → Opens a file in the specified mode ("r", "w", "a", etc.).
2. read(size)            → Reads the entire file or a specific number of bytes (size).
3. readline()            → Reads a single line from the file.
4. readlines()           → Reads all lines and returns them as a list.
5. write(text)           → Writes the given text to the file (overwrites in "w" mode).
6.  writelines(lines)    → Writes multiple lines from a list to the file.
7.  close()              → Closes the file (important to release resources).
8.  seek(offset)         → Moves the file pointer to a specific position.
9.  tell()               → Returns the current position of the file pointer.
10.  flush()             → Immediately writes data to the file without closing it.
11. truncate(size)       → Cuts the file to the specified size bytes.

"""

#  Opening a File in Python

try:
    file = open(r"FileHandling\Git.txt", "r")
    print(file.readline())
except Exception as errror:
    print(errror)
finally:
    file.close()

# Read All data:

try:
    file = open(r"FileHandling\Git.txt", "r")
    for line in file:
        print(line.strip())  # strip() removes extra spaces/newlines
except Exception as errror:
    print(errror)
finally:
    file.close()


#  Writing to a File (w Mode)
# ⚠️ Warning: "w" mode overwrites the file completely!

try:
    f = open(r"FileHandling\Info.txt", "w")
    f.write(
        "Hi There, I'm Vandana & I'm Founder of Horizon!"
    )  # ovverides content (write)
except Exception as errror:
    print(errror)
finally:
    f.close()


# ➕ Appending to a File (a Mode)
# 📝 "a" mode adds content without deleting existing data

try:
    f = open(r"FileHandling\Info.txt", "a")
    f.write(
        "\nHi There, I'm Shiva & I'm CoFounder of Horizon!."
    )  # ovverides content (write)
except Exception as errror:
    print(errror)
finally:
    f.close()


# 🎯 Best Practice: Using with Statement

with open(r"FileHandling\Git.txt", "r") as f:
    content = f.read()
    print(content)  # File closes automatically after this block


# 🔍 Checking if a File Exists:
import os

if os.path.exists(r"FileHandling\Git.txt"):
    print("File Exits!")
else:
    print("File Not Exits!")


# 🛠 Deleting a File
# ⚠️ Be careful! Deleted files cannot be recovered.

import os

file_path = r"FileHandling\Info.txt"

if os.path.exists(file_path):
    os.remove(file_path)
    print("File deleted successfully.")
else:
    print("File not found.")


# 📌 Summary:

# open("file.txt", "mode")       → Opens a file
# read() / readline()            → Reads file content
# write("text") / append("text") → Writes or adds content
# with open(...)                 → Automatically closes file after use
# os.remove("file.txt")          → Deletes a file
