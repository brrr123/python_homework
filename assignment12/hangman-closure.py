def make_hangman(secret_word):
    guesses = []
    
    def hangman_closure(letter):
        guesses.append(letter)

        displayed_word = ""
        for char in secret_word:
            if char in guesses:
                displayed_word += char
            else:
                displayed_word += "_"
        
        print(displayed_word)
        return "_" not in displayed_word
    
    return hangman_closure

if __name__ == "__main__":
    secret_word = input("Enter the secret word: ")

    hangman_game = make_hangman(secret_word)
    guess = input("Enter a letter: ")
    while not hangman_game(guess):
        guess = input("Enter a letter: ")
    
    print("Congratulations! You've guessed the word!")