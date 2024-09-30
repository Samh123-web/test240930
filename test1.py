import random

def three_digit_guess_game():
    # Generate a random three-digit number
    number_to_guess = random.randint(100, 999)
    attempts = 0
    guessed = False

    print("Welcome to the 3-Digit Number Guessing Game!")stgit
    print("Try to guess the number between 100 and 999.")

    while not guessed:
        guess = input("Enter your guess: ")
        
        # Validate input
        if not guess.isdigit() or len(guess) != 3:
            print("Please enter a valid three-digit number.")
            continue
        
        guess = int(guess)
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed = True
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")

# Run the game
three_digit_guess_game()
