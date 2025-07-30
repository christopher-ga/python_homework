def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)
        revealed = ''
        for char in secret_word:
            if char in guesses:
                revealed += char
            else:
                revealed += '_'
        print(revealed)
        return all(char in guesses for char in secret_word)

    return hangman_closure

secret_word = input("Enter the secret word: ")
hangman = make_hangman(secret_word)

while True:
    guess = input("Guess a letter: ")
    if hangman(guess):
        print("Congratulations! You guessed the word.")
        break