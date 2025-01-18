# Level 1 Exercises

# Exercise 1: Age check for driving
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18 - age} more years to learn to drive.")

# Exercise 2: Compare ages with a friend
my_age = 25  # You can change this to your own age
your_age = int(input("Enter your age: "))

if my_age > your_age:
    years_difference = my_age - your_age
    print(f"You are {years_difference} years younger than me." if years_difference > 1 else "You are 1 year younger than me.")
elif my_age < your_age:
    years_difference = your_age - my_age
    print(f"You are {years_difference} years older than me." if years_difference > 1 else "You are 1 year older than me.")
else:
    print("We are the same age.")

# Exercise 3: Compare two numbers
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")


# Level 2 Exercises

# Exercise 1: Grade calculation based on score
score = int(input("Enter your score: "))

if 80 <= score <= 100:
    print("Grade: A")
elif 70 <= score <= 89:
    print("Grade: B")
elif 60 <= score <= 69:
    print("Grade: C")
elif 50 <= score <= 59:
    print("Grade: D")
elif 0 <= score <= 49:
    print("Grade: F")
else:
    print("Invalid score!")

# Exercise 2: Check the season
month = input("Enter a month: ").lower()

if month in ['september', 'october', 'november']:
    print("The season is Autumn.")
elif month in ['december', 'january', 'february']:
    print("The season is Winter.")
elif month in ['march', 'april', 'may']:
    print("The season is Spring.")
elif month in ['june', 'july', 'august']:
    print("The season is Summer.")
else:
    print("Invalid month!")

# Exercise 3: Add a fruit to the list if not present
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit_to_check = input("Enter a fruit: ").lower()

if fruit_to_check not in fruits:
    fruits.append(fruit_to_check)
    print("Updated fruit list:", fruits)
else:
    print("That fruit already exists in the list.")


# Level 3 Exercises

# Exercise 1: Modify and print person dictionary
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Modify the person dictionary as needed
person['age'] = 251  # For example, updating age
person['skills'].append('Django')  # Adding a new skill
person['address']['city'] = 'Helsinki'  # Adding city to the address

# Print modified person dictionary
print("Modified person dictionary:")
print(person)
