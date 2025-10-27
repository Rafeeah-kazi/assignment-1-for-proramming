# Exercise 3: Biography

# Asking the user for input


 # User can type first and last name
name = input("Enter your full name: ")   
hometown = input("Enter your hometown: ")
age_input = input("Enter your age: ")

# Convert age to an integer safely
try:
    age = int(age_input)   # Converts input to integer if possible
except ValueError:         # Runs if input is not a valid number
    age = None             # Use None to indicate unknown age

# Store the information in a dictionary
bio = {
    "Name": name,
    "Hometown": hometown,
    "Age": age
}

# Print the information on separate lines
print(bio["Name"], bio["Hometown"], bio["Age"], sep="\n")