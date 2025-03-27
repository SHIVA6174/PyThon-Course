# for Loop → Used when you know how many times to repeat.
# while Loop → Used when you repeat until a condition is false.

# for()
Coders = ["Vandana", "Shiva", "Chandra Mohan"]
for programer in Coders:
    print(programer)

# range()
for i in range(0, len(Coders)):  # Loops from 1 to 5
    print(Coders[i])

# while Loop – Used for Conditions

count = 1
while count <= 5:
    print(count)
    count += 1  # Increment to avoid infinite loop


#  break and continue – Controlling Loops

# break – Stops the loop
for number in range(1, 10):
    if number == 5:
        break  # Stops when number is 5
    print(number)

# continue – Skips to Next Iteration
for number in range(1, 6):
    if number == 3:
        continue  # Skips when number is 3
    print(number)

#  Nested Loops – Loop Inside Loop

for i in range(1, 3):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"i={i}, j={j}")


# 🎯 Summary
# ✔ for loop → Used when iterating over a sequence (list, tuple, string).
# ✔ while loop → Used when a condition must remain True.
# ✔ break → Stops the loop early.
# ✔ continue → Skips the current iteration.
# ✔ Nested loops → Loop inside another loop.
