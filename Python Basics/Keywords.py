#Python Programme to demonstrate the use of all the important keywords and their use in the program

#The following are the keywords in Python
#False      await      else       import     pass
#None       break      except     in         raise
#True       class      finally    is         return
#and        continue   for        lambda     try
#as         def        from       nonlocal   while
#assert     del        global     not        with
#async      elif       if         or         yield 

#1. False, None, True are used to represent the boolean values in Python
print("--- False, None, True ---")
is_active = True
is_valid = False
result = None
print(f"True: {is_active}, False: {is_valid}, None: {result}")

#2. and, or, not are used for logical operations
print("\n--- and, or, not ---")
x = 10
if x > 5 and x < 20:
    print("x is between 5 and 20")
if x > 15 or x < 5:
    print("x is either greater than 15 or less than 5")
if not (x > 20):
    print("x is not greater than 20")

#3. if, elif, else are used for conditional statements
print("\n--- if, elif, else ---")
age = 18
if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")

#4. for, while are used for loops
print("\n--- for, while ---")
print("for loop:")
for i in range(3):
    print(f"  Iteration {i}")
print("while loop:")
count = 0
while count < 3:
    print(f"  Count: {count}")
    count += 1

#5. break, continue are used to control the flow of loops
print("\n--- break, continue ---")
for i in range(5):
    if i == 2:
        continue
    if i == 4:
        break
    print(f"  i = {i}")

#6. def is used to define a function
print("\n--- def ---")
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

#7. return is used to return a value from a function
print("\n--- return ---")
def add(a, b):
    return a + b

result = add(5, 3)
print(f"5 + 3 = {result}")

#8. import is used to import a module
print("\n--- import ---")
import math
print(f"Square root of 16: {math.sqrt(16)}")

#9. class is used to define a class
print("\n--- class ---")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old"

person = Person("Bob", 25)
print(person.introduce())

#10. pass is used as a placeholder for future code
print("\n--- pass ---")
class EmptyClass:
    pass

print("Empty class created successfully")

#11. raise is used to raise an exception
print("\n--- raise ---")
try:
    x = -5
    if x < 0:
        raise ValueError("Number cannot be negative")
except ValueError as e:
    print(f"Caught exception: {e}")

#12. try, except, finally are used for exception handling
print("\n--- try, except, finally ---")
try:
    num = int("abc")
except ValueError:
    print("ValueError: Could not convert string to integer")
finally:
    print("Cleanup code executed")

#13. with is used to wrap the execution of a block of code within methods defined by a context manager
print("\n--- with ---")
with open("/tmp/test.txt", "w") as file:
    file.write("Hello, World!")
print("File written and closed automatically")

#14. lambda is used to create an anonymous function
print("\n--- lambda ---")
square = lambda x: x ** 2
numbers = [1, 2, 3, 4, 5]
squared = list(map(square, numbers))
print(f"Squared numbers: {squared}")

#15. async, await are used for asynchronous programming
print("\n--- async, await ---")
import asyncio
async def async_function():
    await asyncio.sleep(0)
    return "Async function completed"

print(asyncio.run(async_function()))
