# LISTS IN PYTHON
# A list is an ordered, mutable collection that can store multiple items of different data types

# Creating a list
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
empty_list = []

# LIST FUNCTIONS AND METHODS

# 1. append() - adds an item to the end
fruits.append("mango")
print(fruits)  # ["apple", "banana", "orange", "mango"]

# 2. extend() - adds multiple items from an iterable
fruits.extend(["grape", "kiwi"])
print(fruits)  # ["apple", "banana", "orange", "mango", "grape", "kiwi"]

# 3. insert() - inserts an item at a specific index
fruits.insert(1, "blueberry")
print(fruits)  # ["apple", "blueberry", "banana", ...]

# 4. remove() - removes the first occurrence of an item
fruits.remove("banana")
print(fruits)

# 5. pop() - removes and returns item at index (default: last item)
last_item = fruits.pop()
first_item = fruits.pop(0)

# 6. clear() - removes all items
# fruits.clear()

# 7. index() - returns index of first occurrence
index = fruits.index("blueberry")
print(index)  # 1

# 8. count() - returns number of occurrences
count = numbers.count(3)
print(count)  # 1

# 9. sort() - sorts list in place (ascending order)
numbers.sort()
print(numbers)  # [1, 2, 3, 4, 5]

# 10. reverse() - reverses list in place
numbers.reverse()
print(numbers)  # [5, 4, 3, 2, 1]

# 11. copy() - creates a shallow copy
numbers_copy = numbers.copy()

# ACCESSING ELEMENTS
print(fruits[0])      # First element
print(fruits[-1])     # Last element
print(fruits[1:3])    # Slice from index 1 to 2

# LENGTH
print(len(fruits))    # Number of items in list