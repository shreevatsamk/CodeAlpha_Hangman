import random

# Word categories
categories = {
    'animals': ['elephant', 'giraffe', 'penguin', 'kangaroo', 'zebra', 'chimpanzee'],
    'fruits': ['banana', 'apple', 'grape', 'watermelon', 'pineapple', 'strawberry'],
    'technology': ['developer', 'keyboard', 'laptop', 'network', 'internet', 'software']
}

# Function to choose a random word from the selected category
def choose_word(category):
    return random.choice(categories[category]).lower()

# Function to display the word with underscores for unguessed letters
def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

# Function to display available word categories
def display_categories():
    print("Available categories:")
    for idx, category in enumerate(categories.keys()):
        print(f"{idx + 1}. {category.capitalize()}")
    print()

# Function to give a hint (revealing one random letter)
def give_hint(word, guessed_letters):
    hint_letter = random.choice([letter for letter in word if letter not in guessed_letters])
    print(f"Hint: The word contains the letter '{hint_letter}'.")

# Hangman game with more complexity
def hangman_game():
    # Select difficulty level
    difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
    if difficulty == 'easy':
        tries = 8
    elif difficulty == 'medium':
        tries = 6
    else:  # Default to hard
        tries = 4

    display_categories()
    
    # Let the player choose a category
    category_choice = int(input("Choose a category number: ")) - 1
    category = list(categories.keys())[category_choice]
    
    word = choose_word(category)
    guessed_letters = set()  # To store correct guessed letters
    wrong_guesses = set()    # To store wrong guesses
    score = 0  # Initial score

    print(f"\nYou chose '{category}' category. The word has {len(word)} letters.")
    print(f"You have {tries} incorrect guesses allowed.\n")

    while tries > 0:
        print("Current word:", display_word(word, guessed_letters))
        print("Guessed letters:", ' '.join(sorted(guessed_letters.union(wrong_guesses))))
        print(f"You have {tries} incorrect guesses remaining.\n")

        # Ask if player wants a hint after 3 wrong guesses
        if len(wrong_guesses) >= 3 and input("Do you want a hint? (yes/no): ").lower() == 'yes':
            give_hint(word, guessed_letters)
        
        guess = input("Guess a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters or guess in wrong_guesses:
                print("You already guessed that letter. Try again.\n")
            elif guess in word:
                guessed_letters.add(guess)
                print(f"Good guess! The letter '{guess}' is in the word.\n")
                score += 10  # Increase score for correct guess
                if set(word) == guessed_letters:  # Check if all letters are guessed
                    score += tries * 5  # Bonus points for remaining tries
                    print(f"Congratulations! You guessed the word '{word}'. You win!")
                    print(f"Your final score is: {score}")
                    break
            else:
                wrong_guesses.add(guess)
                tries -= 1
                print(f"Sorry, the letter '{guess}' is not in the word.\n")
        else:
            print("Invalid input. Please guess a single letter.\n")
    
    if tries == 0:
        print(f"Out of guesses! The word was '{word}'. Better luck next time.")
        print(f"Your final score is: {score}")

# Run the game
hangman_game()
