import random

# List of words for the game
word_list = ['Marium','python', 'hangman', 'programming', 'developer','proper']

# Function to choose a random word
def choose_word():
    return random.choice(word_list)

# Function to play Hangman
def play_hangman():
    word = choose_word()  # Choose a random word
    word_length = len(word)
    guessed_word = ['_'] * word_length  # Display underscores for each letter
    guessed_letters = []  # Track guessed letters
    attempts = 10# Number of attempts before losing
    
    print("Welcome to Hangman!")
    print("Try to guess the word:")
    print(" ".join(guessed_word))
    
    # Main game loop
    while attempts > 0:
        guess = input(f"\nYou have {attempts} attempts left. Enter a letter: ").lower()

        # Check if the input is valid (a single letter)
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid letter.")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.append(guess)

        # Check if the guessed letter is in the word
        if guess in word:
            print(f"Good guess! The letter '{guess}' is in the word.")
            
            # Reveal the positions of the guessed letter
            for i in range(word_length):
                if word[i] == guess:
                    guessed_word[i] = guess
                    
            # Display the updated word with guessed letters
            print(" ".join(guessed_word))
        else:
            print(f"Sorry, the letter '{guess}' is not in the word.")
            attempts -= 1  # Decrease attempts on incorrect guess

        # Check if the player has guessed the word
        if '_' not in guessed_word:
            print("\nCongratulations, you've guessed the word!")
            break

    # If attempts run out, the player loses
    if attempts == 0:
        print(f"\nGame over! The word was '{word}'. Better luck next time!")

# Run the game
if __name__ == "__main__":
    play_hangman()
