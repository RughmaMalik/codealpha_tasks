import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']

# 🎯 Predefined word list
word_list = ["python", "codealpha", "developer", "program", "hangman", "project", "script"]

def hangman():
    print("Welcome to Hangman Game")
    print("Try to guess the word before the hangman is complete.")
    print("You have 6 incorrect guesses allowed.\n")

    # Randomly select a word
    chosen_word = random.choice(word_list)
    display_word = ["_"] * len(chosen_word)
    guessed_letters = []
    attempts = 6

    # Main game loop
    while attempts > 0:
        # Display hangman stage and current progress
        print(HANGMANPICS[6 - attempts])
        print("Word:", " ".join(display_word))
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")

        # User input
        guess = input("Enter a letter: ").lower()

        # Input validation
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabet letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.\n")
            continue

        guessed_letters.append(guess)

        # Check if guess is in word
        if guess in chosen_word:
            print("Correct guess!\n")
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    display_word[i] = guess
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.\n")

        # Check if player has guessed all letters
        if "_" not in display_word:
            print("Congratulations! You guessed the word:", chosen_word)
            break

    else:
        # Player ran out of attempts
        print(HANGMANPICS[-1])
        print("Game Over! The correct word was:", chosen_word)

# Run the game
if __name__ == "__main__":
    hangman()
