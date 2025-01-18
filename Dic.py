# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog["name"] = "Buddy"
dog["color"] = "Brown"
dog["breed"] = "Golden Retriever"
dog["legs"] = 4
dog["age"] = 5

# Create a student dictionary and add keys for first_name, last_name, gender, age, marital status, skills, country, city, and address
student = {
    "first_name": "John",
    "last_name": "Doe",
    "gender": "Male",
    "age": 20,
    "marital_status": "Single",
    "skills": ["Python", "Java", "SQL"],
    "country": "USA",
    "city": "New York",
    "address": "123 Main St"
}

# Get the length of the student dictionary
student_length = len(student)

# Get the value of skills and check the data type
skills = student["skills"]
skills_type = type(skills)

# Modify the skills values by adding one or two skills
student["skills"].extend(["Docker", "Kubernetes"])

# Get the dictionary keys as a list
student_keys = list(student.keys())

# Get the dictionary values as a list
student_values = list(student.values())

# Change the dictionary to a list of tuples using items() method
student_items = list(student.items())

# Delete one of the items in the dictionary
del student["address"]

# Delete the entire student dictionary
del student

# Print the results
print("Dog Dictionary:", dog)
print("Student Dictionary Length:", student_length)
print("Skills:", skills)
print("Data Type of Skills:", skills_type)
print("Student Keys:", student_keys)
print("Student Values:", student_values)
print("Student Items:", student_items)
