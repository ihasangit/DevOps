# --- Python Concepts Implementation from Notes --- #

# Concatenation
greeting = "Hello" + " " + "World!"
print(greeting)  # Output: Hello World!

# Repetition
repeated = "Hello! " * 3
print(repeated)  # Output: Hello! Hello! Hello!

# String length
length = len("Hello")
print(length)  # Output: 5

# Case conversion
string = "hello"
print(string.upper())       # Output: HELLO
print(string.capitalize())  # Output: Hello
print(string.lower())       # Output: hello

# Formatting with placeholders
name = "Alice"
age = 25
pi = 3.14159
print("Name: %s, Age: %d, Pi: %.2f" % (name, age, pi))  
# Output: Name: Alice, Age: 25, Pi: 3.14

# Reversing a string
string = "Python"
reversed_string = string[::-1]
print(reversed_string)  # Output: nohtyP

# List
my_list = [1, 2, 3, 4]
print(my_list)  # Output: [1, 2, 3, 4]

# Tuple
my_tuple = (1, 2, 3, 4)
print(my_tuple)  # Output: (1, 2, 3, 4)

# Set
my_set = {1, 2, 3, 4, 4}
print(my_set)  # Output: {1, 2, 3, 4}

# Dictionary
my_dict = {"name": "Alice", "age": 25}
print(my_dict)  # Output: {'name': 'Alice', 'age': 25}

# CRUD Operations
# Create
data = {"id": 1, "name": "John"}
print("Create:", data)

# Read
print("Read:", data["name"])

# Update
data["name"] = "John Doe"
print("Update:", data)

# Delete
del data["name"]
print("Delete:", data)

# JSON Example
import json
json_data = {
    "name": "John",
    "age": 30,
    "isStudent": False,
    "courses": ["Math", "Science"]
}
json_string = json.dumps(json_data)  # Convert Python dict to JSON string
print(json_string)

# Binary Conversion
number = 13
binary = bin(number)[2:]  # Convert number to binary
print(f"{number} in binary is {binary}")  # Output: 13 in binary is 1101

# Horizontal vs Vertical Scaling Example
print("Horizontal Scaling: Add more machines.")
print("Vertical Scaling: Upgrade the current machine.")

# CAP Theorem Simplified
print("CAP Theorem: Choose two - Consistency, Availability, Partition Tolerance.")

# Cache Example
cache = {}
cache["search_result"] = "Fast Data"
print("Cache:", cache)

# Load Balancing Simulation
requests = [1, 2, 3, 4, 5]
balanced = [[req] for req in requests]  # Simulate distributing requests
print("Load Balanced Requests:", balanced)

# Sharding Example
data = list(range(1, 11))
shard1, shard2 = data[:5], data[5:]
print("Shard 1:", shard1)
print("Shard 2:", shard2)

# Source Control Commands (as comments for Git Workflow)
# Initialize repository
# git init
# Add files
# git add .
# Commit changes
# git commit -m "Initial commit"
# Push to GitHub
# git push origin main

# Debugging Example
try:
    result = 10 / 0  # Division by zero error
except ZeroDivisionError as e:
    print(f"Debugging Error: {e}")

# Variables and Data Structures
name = "Alice"
age = 25
height = 5.6
is_student = True
print(f"Name: {name}, Age: {age}, Height: {height}, Student: {is_student}")

# End of the Python Notes Implementation
