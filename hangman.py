print("Welcome to Hangman")

import random

#this sets the random word list and selects a random word each time we play the game
words = ['apple' , 'banana' , 'orange' , 'strawberry' , 'blueberry' , 'kiwi' , 'raspberry' , 'grapes' , 'peach', 'plum' , 'nectarine' , 'cherry' , 'pear' , 'lemon' , 'lime']
secret_word = random.choice(words)

# --- Step 2: Set Up the Game State ---
guessed_letters = []
incorrect_guesses = 0
max_guesses = 10

# --- Step 3: Initialize the Display Word ---
display_word = ['_'] * len(secret_word)

print("Welcome to Hangman!")

# --- Step 4: The Main Game Loop ---
while incorrect_guesses < max_guesses:
    # Display the current state of the game
    print("\n" + " ".join(display_word))
    print(f"Incorrect guesses remaining: {max_guesses - incorrect_guesses}")
    print(f"Guessed letters: {', '.join(guessed_letters)}")

    # Get the player's guess
    guess = input("Guess a letter: ").lower()

    # Check for invalid input (e.g., more than one character)
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        continue

    # Check if the player already guessed this letter
    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue

    # Add the new guess to the list
    guessed_letters.append(guess)

    # Check if the guess is in the secret word
    if guess in secret_word:
        print("Good guess!")
        # Update the display_word
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        print("Incorrect guess.")
        incorrect_guesses += 1

    # --- Step 5: Check for a Win Condition ---
    if '_' not in display_word:
        break  # Exit the loop if all letters are revealed

# --- Step 6: Finalizing the Game ---
print("\n" + " ".join(display_word))

if '_' not in display_word:
    print(f"Congratulations! You guessed the word, {secret_word}")
else:
    print(f"Game over! The word was {secret_word}")
