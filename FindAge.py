from datetime import datetime

# Function to calculate age
def calculate_age(birth_year):
    current_year = datetime.now().year
    age = current_year - birth_year
    return age

birth_year = 2004
age = calculate_age(birth_year)
print(f"You are {age} years old.")
