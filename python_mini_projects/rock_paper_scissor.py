import random

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    user_input = input("Enter rock, paper, or scissors: ").strip().lower()
    while user_input not in choices:
        print("Invalid choice. Try again.")
        user_input = input("Enter rock, paper, or scissors: ").strip().lower()
    return user_input

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    # (\) line continuation character in Python.
    # It tells Python that the statement continues on the next line,
    # allowing you to split long logical conditions across
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))
        play_again = input("Play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

play()