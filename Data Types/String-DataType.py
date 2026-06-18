# String Data Type in Python

# Creating strings
name = "Hello"
message = 'Python Programming'
multiline = """This is a
multiline string"""

print("String examples:")
print(name)
print(message)
print(multiline)

# Accessing single characters from a string
# Strings are indexed starting from 0
print("\n--- Accessing Characters ---")
text = "Python"

print(f"First character: {text[0]}")      # P
print(f"Second character: {text[1]}")     # y
print(f"Third character: {text[2]}")      # t

# Negative indexing (from the end)
print(f"Last character: {text[-1]}")      # n
print(f"Second last: {text[-2]}")         # o

# String slicing
print(f"\nFirst 3 characters: {text[0:3]}")  # Pyt
print(f"From index 2 onwards: {text[2:]}")  # thon