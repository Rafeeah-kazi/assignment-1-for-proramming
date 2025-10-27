# Exercise: Simple Search

# List of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Ask user for a name to search
search = input("Enter a name to search (press Enter to search for Sam): ")

# Use "Sam" if user doesn't type anything
if not search:
    search = "Sam"

# Check if the name is in the list
if search in names:
    print(search + " was found in the list!")
else:
    print(search + " was not found in the list.")

    
    
    