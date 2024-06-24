import random

def get_user_name():
    user_name = input("Hey! What's your name?").lower()
    while user_name.isnumeric():
        user_name = input("Invalid. Enter name: ").lower()
    return user_name.capitalize()
        
def get_user_choice():
    user_choice = input("What do you choose?(rock, paper, scissors): ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        user_choice = input("Invalid choice. Enter choice (rock, paper, scissors): ").lower()
    return user_choice

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_name = get_user_name()
    print(f"Let's play Rock Paper Scissors, {user_name}!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(determine_winner(user_choice, computer_choice))

if __name__ == "__main__":
    play_game()
