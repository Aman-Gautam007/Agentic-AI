# A set is an unordered, unindexed collection of unique elements
# Sets are mutable and use curly braces {}

# Creating Sets
my_set = {1, 2, 3, 4, 5}
empty_set = set()  # Note: {} creates a dict, not a set
set_from_list = set([1, 2, 2, 3])  # Duplicates removed automatically

# Note: set() accepts only ONE iterable argument
# set([1,2,2,3], [2,4,4,6]) raises TypeError: set expected at most 1 argument, got 2
# To combine multiple lists into a set, use one of these methods:
set_method1 = set([1,2,2,3] + [2,4,4,6])  # Concatenate lists first
print("Method 1 (concatenate):", set_method1)  # {1, 2, 3, 4, 6}

set_method2 = set([1,2,2,3]) | set([2,4,4,6])  # Use union operator
print("Method 2 (union):", set_method2)  # {1, 2, 3, 4, 6}

set_method3 = set([1,2,2,3])
set_method3.update([2,4,4,6])  # Use update method
print("Method 3 (update):", set_method3)  # {1, 2, 3, 4, 6}

# Adding Elements
my_set.add(6)
my_set.update([7, 8, 9])

# Removing Elements
my_set.remove(5)  # Raises KeyError if not found
my_set.discard(10)  # No error if not found
popped = my_set.pop()  # Removes and returns arbitrary element
my_set.clear()  # Removes all elements

# Set Operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union = set1 | set2  # or set1.union(set2)
print("Union:", union)  # {1, 2, 3, 4, 5, 6}
intersection = set1 & set2  # or set1.intersection(set2)
print("Intersection:", intersection)  # {3, 4}
difference = set1 - set2  # or set1.difference(set2)
print("Difference:", difference)  # {1, 2}
sym_difference = set1 ^ set2  # or set1.symmetric_difference(set2)
print("Symmetric Difference:", sym_difference)  # {1, 2, 5, 6}

# Set Comparisons
is_subset = set1 <= set2  # or set1.issubset(set2)
is_superset = set1 >= set2  # or set1.issuperset(set2)
is_disjoint = set1.isdisjoint(set2)

# Checking Membership
if 2 in set1:
    print("Element exists")

# Iterating
for element in set1:
    print(element)

# Copying
set_copy = set1.copy()

# Length and Conversion
length = len(set1)
print("Length of set1:", length)
list_from_set = list(set1)
print("List from set:", list_from_set)
print("Set from list:", set_from_list)