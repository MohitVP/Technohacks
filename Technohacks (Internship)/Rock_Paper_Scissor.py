import random

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter your choice:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    choices = ["rock", "paper", "scissors"]
    user_choice = int(input("Your choice (1-3): ")) - 1

    if user_choice < 0 or user_choice > 2:
        print("Invalid choice. Please try again.")
        return

    computer_choice = random.randint(0, 2)

    print("You chose:", choices[user_choice])
    print("Computer chose:", choices[computer_choice])

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == 0 and computer_choice == 2)
        or (user_choice == 1 and computer_choice == 0)
        or (user_choice == 2 and computer_choice == 1)
    ):
        print("You win!")
    else:
        print("Computer wins!")

while True:
    play_game()
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break

print("Thanks for playing!")
