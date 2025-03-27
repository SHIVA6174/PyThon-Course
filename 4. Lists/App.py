"""
🔹 Definition of a List in Python 🚀
A list in Python is an ordered, mutable collection that can store multiple items of different data types (integers, strings, floats, etc.). Lists allow adding, removing, and modifying elements dynamically.

📌 Key Properties:
✔ Ordered → Maintains the order of elements.
✔ Mutable → Elements can be changed after creation.
✔ Allows Duplicates → Can store multiple occurrences of the same value.
✔ Heterogeneous → Can contain different data types in a single list.

"""


# 📝 Adding & Removing Elements

fruits = ["apple", "banana"]
fruits.append("cherry")  # ['apple', 'banana', 'cherry']
fruits.extend(["grape", "mango"])  # ['apple', 'banana', 'cherry', 'grape', 'mango']
fruits.insert(1, "orange")  # ['apple', 'orange', 'banana', 'cherry', 'grape', 'mango']
fruits.remove("banana")  # ['apple', 'orange', 'cherry', 'grape', 'mango']
print(fruits.pop(2))  # 'cherry' (removes and returns the element)
fruits.clear()  # []


# Searching & Counting

nums = [10, 20, 30, 20, 40, 50]

print(nums.index(20))  # 1 (first occurrence)
print(nums.count(20))  # 2 (number of times 20 appears)


# Modifying Lists

nums = [3, 1, 4, 1, 5, 9]
nums.sort()  # [1, 1, 3, 4, 5, 9]
nums.reverse()  # [9, 5, 4, 3, 1, 1]
copy_nums = nums.copy()  # Creates a new list with the same elements

#  List Length & Summing

numbers = [5, 10, 15, 20]

print(len(numbers))  # 4 (number of elements)
print(sum(numbers))  # 50 (sum of all elements)
print(min(numbers))  # 5 (smallest element)
print(max(numbers))  # 20 (largest element)

# List Iteration & Conversion
text = ["Python", "is", "fun"]
sentence = " ".join(text)  # 'Python is fun'
num_list = list(range(1, 6))  # [1, 2, 3, 4, 5]


#  Other Methods
nums = [1, 2, 3, 4, 5]

print(any(nums))  # True (at least one non-zero value)
print(all(nums))  # True (all elements are non-zero)


"""
###  📝 Adding & Removing Elements 
 `append(element)`  → Adds an element to the end of the list.  
 `extend(iterable)`  → Adds all elements of an iterable (e.g., list, tuple) to the end.  
 `insert(index, element)`  → Inserts an element at a specific index.  
 `remove(element)`  → Removes the first occurrence of an element.  
 `pop(index)`  → Removes and returns the element at the specified index (default is the last element).  
 `clear()`  → Removes all elements from the list.  

###  🔍 Searching & Counting 
 `index(element)`  → Returns the index of the first occurrence of the element.  
 `count(element)`  → Returns the number of times an element appears in the list.  

###  🛠 Modifying Lists 
 `sort()`  → Sorts the list in ascending order (modifies the list).  
 `reverse()`  → Reverses the order of the list in-place.  
 `copy()`  → Returns a shallow copy of the list (similar to slicing).  



###  📏 List Length & Summing 
 `len(list)`  → Returns the number of elements in the list.  
 `sum(list)`  → Returns the sum of all elements (if they are numbers).  
 `min(list)`  → Returns the smallest element.  
 `max(list)`  → Returns the largest element.  
 `any()`  → Returns `True` if any element is `True` in the list.  
 `all()`  → Returns `True` if all elements are `True` in the list.  


###  🔗 List Iteration & Conversion 
 `join(iterable)`  → Joins elements of an iterable into a string (useful for strings).  
 `list()`  → Converts an iterable into a list.  

###  🎯 Other Methods 
 `sort(reverse=True)`  → Sorts the list in descending order.  
 `index(element, start, end)`  → Returns the index of the first occurrence of `element` in the slice `list[start:end]`.  

###  🔥 Summary 
✔  Add/Remove Elements  → `append(), extend(), remove(), pop()`  
✔  Modify List  → `sort(), reverse(), copy()`  
✔  Search & Count  → `index(), count()`  
✔  Length & Sum  → `len(), sum(), min(), max()`  
✔  Join & Convert  → `join(), list()`  
"""
