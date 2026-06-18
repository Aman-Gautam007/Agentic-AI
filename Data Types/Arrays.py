import array
import numpy as np

#Arrays in Python - Comprehensive Documentation
'''
DEFINITION:
Arrays in Python are ordered collections of elements stored in contiguous memory 
locations. While Python doesn't have a built-in 'array' type like some languages, 
the primary array-like structures are lists and the 'array' module from the 
standard library.

MAIN ARRAY STRUCTURES:

1. Lists (Most Common):
    - Dynamic, mutable sequences
    - Can store mixed data types
    - Indexed from 0

2. Array Module:
    - Type-restricted arrays (single data type)
    - More memory-efficient than lists
    - Requires: import array

3. NumPy Arrays:
    - Multi-dimensional arrays
    - Optimized for numerical computing
    - Requires: import numpy

KEY FUNCTIONALITIES:

CREATION:
- list(): Create empty or from iterable
- array.array(): Create typed array
- numpy.array(): Create NumPy array
- List comprehension: [x for x in range(n)]

ACCESS & MODIFICATION:
- Indexing: arr[0], arr[-1]
- Slicing: arr[1:5], arr[::2]
- append(): Add element at end
- insert(index, value): Insert at position
- remove(value): Remove first occurrence
- pop(index): Remove and return element
- extend(iterable): Add multiple elements

SEARCHING & SORTING:
- index(value): Find first occurrence
- count(value): Count occurrences
- sort(): Sort in-place
- reverse(): Reverse in-place
- sorted(): Return sorted copy

ITERATION:
- for loop: Direct iteration
- enumerate(): Index and value pairs
- zip(): Combine multiple arrays

PROPERTIES:
- len(arr): Array length
- min(arr), max(arr): Min/max values
- sum(arr): Sum of elements
- all(), any(): Boolean aggregation

ADVANCED OPERATIONS:
- map(), filter(): Functional programming
- list comprehension: Concise iteration
- Multi-dimensional indexing (NumPy)
- Broadcasting (NumPy)

MEMORY & PERFORMANCE:
- Lists: Flexible, slower
- array module: Fixed type, faster
- NumPy: Vectorized operations, fastest
'''
# EXAMPLES:

# 1. LISTS - Creation and Basic Operations
my_list = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True]
list_from_range = list(range(5))  # [0, 1, 2, 3, 4]

# 2. ACCESSING ELEMENTS
first = my_list[0]  # 1
last = my_list[-1]  # 5
slice_result = my_list[1:4]  # [2, 3, 4]
every_other = my_list[::2]  # [1, 3, 5]

# 3. MODIFYING LISTS
my_list.append(6)  # [1, 2, 3, 4, 5, 6]
my_list.insert(0, 0)  # [0, 1, 2, 3, 4, 5, 6]
my_list.remove(3)  # Removes first occurrence of 3
popped = my_list.pop()  # Removes and returns last element
my_list.extend([7, 8])  # Add multiple elements

# 4. SEARCHING & SORTING
index = my_list.index(2)  # Returns index of 2
count = my_list.count(1)  # Returns count of 1s
my_list.sort()  # Sort in-place
sorted_copy = sorted(my_list, reverse=True)  # Returns sorted copy

# 5. ITERATION
for item in my_list:
    print(item)

for i, value in enumerate(my_list):
    print(f"Index {i}: {value}")

# 6. ARRAY MODULE - Type-restricted arrays
typed_array = array.array('i', [1, 2, 3, 4, 5])  # 'i' = signed integer

# 7. LIST COMPREHENSION
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# 8. NUMPY ARRAYS
np_array = np.array([1, 2, 3, 4, 5])
matrix = np.array([[1, 2, 3], [4, 5, 6]])
zeros = np.zeros((3, 3))
ones = np.ones((2, 4))

# 9. PROPERTIES
length = len(my_list)  # 7
minimum = min(my_list)
maximum = max(my_list)
total = sum(my_list)

# 10. FUNCTIONAL PROGRAMMING
doubled = list(map(lambda x: x * 2, my_list))
filtered = list(filter(lambda x: x > 2, my_list))

# 11. ZIP - Combine arrays
arr1 = [1, 2, 3]
arr2 = ['a', 'b', 'c']
combined = list(zip(arr1, arr2))  # [(1, 'a'), (2, 'b'), (3, 'c')]
