"""
    Author: Rayhan Hossain
    Date created: 01/02/2024
    Last modified: 01/02/2024
    Python Version: 3.12
"""

import random
from hangman_words import word_list
from hangman_art import logo, stages

# Generate a random word from hangman
word_choice = random.choice(word_list)
print(f"Your word is: {word_choice}")
# Print hangman
print(logo)

# Generate as many blanks as letters in word
blanks = []
for letter in word_choice:
    blanks.append("_")

# Set the game as False
game_over = False

# Set 7 lives
lives = 7

# Run the game until the game_over = True
while not game_over:

    # Asks user to enter a letter
    guess = input("Guess a letter: ").lower()

    # Tell the user if they've already guessed that letter
    if guess in blanks:
        print("You've already guessed that letter.")

    # Fill the blanks with the guessed word
    for position in range(len(word_choice)):
        if guess == word_choice[position]:
            blanks[position] = guess

    # Join the blanks in f-string
    print(f"{' '.join(blanks)}")

    # End the game if all the blanks are filled
    if "_" not in blanks:
        game_over = True
        print("You won!")

    # If the letter doesn't exist in the word, deduct a life and draw the hangman
    if guess not in word_choice:
        print(f"You guessed '{guess}' which doesn't exist in the word. Hence, you lose a life!")
        lives -= 1

        # If no life is left, end the game
        if lives == 0:
            print("You don't have any life remaining. You've lost the game!")
            game_over = True

    # Display hangman if at least one life is lost
    if lives < 7:
        print(stages[lives])
