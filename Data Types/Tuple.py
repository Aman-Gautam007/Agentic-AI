# TUPLES IN PYTHON

# What is a Tuple?
# A tuple is an immutable, ordered collection of elements enclosed in parentheses.
# Unlike lists, tuples cannot be modified after creation (no add, remove, or change).
# Tuples are faster and use less memory than lists.

# Creating a Tuple
my_tuple = (1, 2, 3, 4, 5)
mixed_tuple = (1, "hello", 3.14, True)
single_element_tuple = (42,)  # Note: comma is required for single element
empty_tuple = ()

print("Tuple:", my_tuple)
print("Mixed Tuple:", mixed_tuple)

# Tuple Functions and Methods

# 1. len() - Returns the number of elements
print("\nLength:", len(my_tuple))

# 2. count() - Counts occurrences of a value
numbers = (1, 2, 2, 3, 2, 4)
print("Count of 2:", numbers.count(2))

# 3. index() - Returns the index of first occurrence
print("Index of 3:", numbers.index(3))

# 4. Indexing - Access elements by index
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# 5. Slicing - Extract a portion of the tuple
print("Slice [1:3]:", my_tuple[1:3])

# 6. Unpacking - Assign tuple elements to variables
a, b, c, d, e = my_tuple
print("Unpacked values:", a, b, c)

# 7. Concatenation - Combine tuples
tuple1 = (1, 2)
tuple2 = (3, 4)
combined = tuple1 + tuple2
print("Concatenated:", combined)

# 8. Repetition - Repeat tuple elements
repeated = my_tuple[:3] * 2
print("Repeated:", repeated)

# 9. Membership - Check if element exists
print("Is 3 in tuple?", 3 in my_tuple)

# 10. Iteration - Loop through tuple
print("Iterating:")
for item in my_tuple:
    print(item, end=" ")