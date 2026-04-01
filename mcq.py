score = 0
print("Welcome to the MCQ Quiz!\n")
print("Q1: Which keyword is used to define a function in Python?")
print("1. func")
print("2. def")
print("3. function")
print("4. lambda")
ans1 = int(input("Enter your choice (1-4): "))
if ans1 == 2:
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer is 'def'\n")
print("Q2: Which of these is a mutable data type?")
print("1. Tuple")
print("2. List")
print("3. String")
print("4. Integer")
ans2 = int(input("Enter your choice (1-4): "))
if ans2 == 2:
    print("Correct!\n")
    score += 1
else:
    print(" Wrong! Correct answer is 'List'\n")
print("Q3: What does OOP stand for?")
print("1. Object-Oriented Programming")
print("2. Order Of Program")
print("3. Open Operational Process")
print("4. None")
ans3 = int(input("Enter your choice (1-4): "))
if ans3 == 1:
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer is 'Object-Oriented Programming'\n")
print("Quiz Finished!")
print(f"Your Score: {score}/3")
