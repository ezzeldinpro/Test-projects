import random
import time

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        # Difficulty selection
        print("\nPlease select the difficulty level:")
        print("1. Easy (10 chances)")
        print("2. Medium (5 chances)")
        print("3. Hard (3 chances)")
        
        difficulty = input("Enter your choice: ")
        if difficulty == "1":
            chances = 10
            print("\nGreat! You have selected the Easy difficulty level.")
        elif difficulty == "2":
            chances = 5
            print("\nGreat! You have selected the Medium difficulty level.")
        elif difficulty == "3":
            chances = 3
            print("\nGreat! You have selected the Hard difficulty level.")
        else:
            print("Invalid choice. Please select again.")
            continue
        
        print(f"You have {chances} chances to guess the correct number.")
        print("Let's start the game!")

        # Generate random number
        secret_number = random.randint(1, 100)
        attempts = 0
        start_time = time.time()

        while chances > 0:
            try:
                guess = int(input("\nEnter your guess: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            attempts += 1
            if guess == secret_number:
                end_time = time.time()
                print(f"\nCongratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
                print(f"It took you {round(end_time - start_time, 2)} seconds.")
                break
            elif guess < secret_number:
                print("Incorrect! The number is greater than your guess.")
            else:
                print("Incorrect! The number is less than your guess.")
            
            chances -= 1
            print(f"You have {chances} chances left.")

        if chances == 0:
            print(f"\nGame Over! The correct number was {secret_number}.")

        # Play again prompt
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    number_guessing_game()
