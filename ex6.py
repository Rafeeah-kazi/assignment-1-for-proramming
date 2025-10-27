# Excercise 6 - Define the correct password

correct_password = "3672"

#asking the user for password until its correct

while True:
    entered_password = input("Enter the password: ")
    if entered_password == correct_password:
        print("Access granted! Welcome!")
        break  # Exit the loop when the password is correct
    else:
        print("Incorrect password. Try again.")
        


