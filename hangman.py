print("Welcome to Hangman")

import random

#this sets the random word list and selects a random word each time we play the game
words = ['apple' , 'banana' , 'orange' , 'strawberry' , 'blueberry' , 'kiwi' , 'raspberry' , 'grapes' , 'peach', 'plum' , 'nectarine' , 'cherry' , 'pear' , 'lemon' , 'lime']
secret_word = random.choice(words)

#this sets the game state
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

#create the list of underscores for each letter in secret_word
display_word = ['_'] * len(secret_word)

#strings that show each stage of the hangman
hangman_stages = [
    """
       -----
       |   |
       |   
       |  
       |   
       |    
    --------
    """,
    """
       -----
       |   |
       |   O
       |  
       |   
       |    
    --------
    """,
    """
       -----
       |   |
       |   O
       |   |
       |   
       |    
    --------
    """,
    """
       -----
       |   |
       |   O
       |  /|
       |  
       |    
    --------
    """,
    """
       -----
       |   |
       |   O
       |  /|\
       |  
       |    
    --------
    """,
    """
       -----
       |   |
       |   O
       |  /|\
       |  / 
       |    
    --------
    """,
    """
       -----
       |   |
       |   O
       |  /|\
       |  / \
       |    
    --------
    """
]


#show the player what they're guessing
print("".join(display_word))
print(hangman.stages[incorrect_guesses])

#the main game loop
while incorrect_guesses < max_guesses:
    print("\n" + " ".join(display_word))
    print(f"Incorrect guesses remaining: {max_guesses - incorrect_guesses}")

    #get the player's guess
    guess = input("Guess a letter: ").lower()

    #checks if the player already guessed the letter
    if guess in guessed_letters:
        print("You already guessed this letter. Try another.")
        continue #skips the rest of the loop and starts over

    #add the new guess to the list of guessed letters
    guessed_letters.append(guess)

    #check if guessed letter is in the secret word
    if guess in secret_word:
        print("Good guess!")
        #updates the display word
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        print ("Incorrect guess.")
        incorrect_guesses += 1

    #check for a win condition
    if '_' not in display_word:
        break #exit the loop if all letters revealed

#finalize the game
print("\n" + " ".join(display_word))

if '_' not in display_word:
    print(f"Congratulations! You are a winner. The word was {secret_word}")
else:
    print(f"Game over. The word was {secret_word}")

    
