print("Welcome to the Quiz Game!")
playing = input("Want to play game? (yes/no): ").lower()
if playing != "yes":
    print("Exiting the game. Goodbye!")
    exit()
print("Let's start the game!")
score = 0

answer = input("What is the capital of India? ").lower()
if answer == "new delhi":
    print("Correct!")
    score += 1
    
else:
    print("Incorrect! The correct answer is New Delhi.")

answer = input("What is the capital of Pakistan? ").lower()
if answer == "islamabad":
    print("Correct!")
    score += 1
    
else:
    print("Incorrect! The correct answer is islamabad.")

answer = input("What is GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
    
else:
    print("Incorrect! The correct answer is graphics processing unit.")

answer = input("What is stand for RAM? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
    
else:
    print("Incorrect! The correct answer is random access memory.")

print("Thanks for playing the game!")
print(f"Your score is {score}/4")
exit()
