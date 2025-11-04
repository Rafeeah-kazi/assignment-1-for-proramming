# Exercise 7 with user input


# 1. Count up from 0 to 50

"""
# Display a message to indicate what the loop will do
Print each number in the loop
Loop from 0 to 50 (range stops before 51)
"""

print("Counting up from 0 to 50:")  
for i in range(0, 51):             
    print(i)             

"""
 Loop from 50 down to 0 (step of -1)
print each number in the loop
"""          
# 2. Count down from 50 to 0
print("Counting down from 50 to 0:")  
for i in range(50, -1, -1):          
    print(i)

# 3. Count up from 30 to 50
print("Counting up from 30 to 50:") 
for i in range(30, 51):          # Loop from 30 to 50
    print(i)                     # Print each number

# 4. Count down from 50 to 10 by 2
print("Counting down from 50 to 10 by 2:") 

# Loop from 50 down to 10, decreasing by 2 each time
for i in range(50, 9, -2):                  
    print(i)                                 

# 5. Count up from 100 to 200 by 5
print("Counting up from 100 to 200 by 5:")  
for i in range(100, 201, 5): # Loop from 100 to 200, increasing by 5 each time
    print(i)                                

print("Done!")  # all counting loops are finished
