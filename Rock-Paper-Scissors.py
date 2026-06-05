import random

# Welcome Message
print("=== ROCK, PAPER, SCISSORS ===")

# Keep track of scores
user_score = 0
computer_score = 0

# Game Options
options = ["rock", "paper", "scissors"]

# Start a loop so the game keeps playing
while True:
    print("\n--- New Round ---")
    user_choice = input("Choose rock, paper, or scissors (or type 'quit' to exit): ").lower().strip()

    # Check if user wants to stop playing
    if user_choice == 'quit':
        print("\nThanks for playing!")
        print(f"Final Score -> You: {user_score} | Computer: {computer_score}")
        break

    # Check if user typed a valid move
    if user_choice not in options:
        print("Invalid choice! Please type rock, paper, or scissors.")
        continue

    # Computer makes a random choice
    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    # Game Logic: Check for a tie
    if user_choice == computer_choice:
        print("It's a tie!")

    # Game Logic: Check all ways the user can WIN
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
        print("You win this round! 🎉")
        user_score += 1

    # If it's not a tie and you didn't win, you lost
    else:
        print("You lose this round! 😢")
        computer_score += 1

    # Display the current score
    print(f"Score -> You: {user_score} | Computer: {computer_score}")