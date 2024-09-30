import random

def generate_number():
    """Generate a random 3-digit number with unique digits."""
    digits = random.sample(range(10), 3)  # Get 3 unique digits
    return ''.join(map(str, digits))

def get_feedback(guess, number):
    """Return feedback in the form of A and B."""
    A = sum(1 for i in range(3) if guess[i] == number[i])
    B = sum(1 for digit in guess if digit in number) - A
    return A, B

def number_guess_game():
    number_to_guess = generate_number()
    attempts = 0
    guessed = False

    print("Welcome to the Number Guess A?B Game!")
    print("Guess the 3-digit number (with unique digits).")

    while not guessed:
        guess = input("Enter your guess: ")

        # Validate input
        if len(guess) != 3 or not guess.isdigit() or len(set(guess)) != 3:
            print("Please enter a valid 3-digit number with unique digits.")
            continue

        attempts += 1
        A, B = get_feedback(guess, number_to_guess)

        if A == 3:
            guessed = True
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        else:
            print(f"{A}A {B}B - Keep trying!")

# Run the game
number_guess_game()
