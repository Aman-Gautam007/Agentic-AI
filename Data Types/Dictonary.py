# DICTIONARY DEFINITION AND FEATURES

# 1. Creating a Dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}
empty_dict = {}
dict_constructor = dict(name="John", age=30)

# 2. Key Features
# - Unordered (Python 3.7+: ordered by insertion)
# - Mutable (can be modified)
# - Keys must be immutable (strings, numbers, tuples)
# - Values can be any data type

# 3. Accessing Elements
print(my_dict["name"])  # Direct access
print(my_dict.get("age"))  # Safe access (returns None if key doesn't exist)

# 4. Common Dictionary Methods

# keys() - returns all keys
print(my_dict.keys())

# values() - returns all values
print(my_dict.values())

# items() - returns key-value pairs
print(my_dict.items())

# get() - safely retrieve value
print(my_dict.get("name", "default"))

# pop() - remove and return value
my_dict.pop("city")

# popitem() - remove last inserted item
my_dict.popitem()

# clear() - remove all items
my_dict.clear()

# update() - merge dictionaries
my_dict.update({"name": "Jane", "age": 25})

# copy() - create shallow copy
dict_copy = my_dict.copy()

# setdefault() - get value or set default
my_dict.setdefault("country", "USA")

# 5. Iteration
for key in my_dict:
    print(key, my_dict[key])

for key, value in my_dict.items():
    print(key, value)

# 6. Check membership
print("name" in my_dict)  # True
print("email" in my_dict)  # False