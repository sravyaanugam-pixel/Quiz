print("===================================")
print("   GENERAL KNOWLEDGE QUIZ")
print("===================================\n")

score = 0

# Question 1
answer = input("1. What is the capital of India? ").strip().lower()
if answer == "new delhi":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer: New Delhi\n")

# Question 2
answer = input("2. Which planet is known as the Red Planet? ").strip().lower()
if answer == "mars":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer: Mars\n")

# Question 3
answer = input("3. Who wrote 'Romeo and Juliet'? ").strip().lower()
if answer == "william shakespeare":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer: William Shakespeare\n")

# Question 4
answer = input("4. How many continents are there in the world? ").strip().lower()
if answer == "7":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer: 7\n")

# Question 5
answer = input("5. What is the largest ocean in the world? ").strip().lower()
if answer == "pacific ocean":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer: Pacific Ocean\n")

# Question 6
answer = input("6. Which is the national animal of India? ").strip().lower()
if answer == "tiger":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer: Tiger\n")

# Question 7
answer = input("7. Who is known as the Father of the Nation in India? ").strip().lower()
if answer == "mahatma gandhi":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer: Mahatma Gandhi\n")

# Question 8
answer = input("8. Which is the largest planet in our solar system? ").strip().lower()
if answer == "jupiter":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer: Jupiter\n")

# Question 9
answer = input("9. Which gas do plants absorb from the atmosphere? ").strip().lower()
if answer == "carbon dioxide":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer: Carbon Dioxide\n")

# Question 10
answer = input("10. How many days are there in a leap year? ").strip().lower()
if answer == "366":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer: 366\n")

print("===================================")
print("Quiz Completed!")
print("Your Score:", score, "/10")

if score == 10:
    print("Excellent! Perfect Score!")
elif score >= 8:
    print("Very Good!")
elif score >= 5:
    print("Good Job!")
else:
    print("Keep Practicing!")

print("===================================")