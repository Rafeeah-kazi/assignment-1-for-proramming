# Exercise 4: Primitive Quiz

answer = input("What is the capital of France? ")

#for the basic version
if answer == "Paris":      #it's the condition for true
    print("Corrrect! ")
else:                      #it's the condition for fales
    print("Wrong! The correct answer is Paris.")
    
    
# Advanced version


quiz = {
    quiz = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
    "Switzerland": "Bern"
}

score = 0  # To count correct answers

# Ask each question
for country in quiz:
    answer = input(f"What is the capital of {country}? ")
    if answer.lower() == quiz[country].lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {quiz[country]}.")


