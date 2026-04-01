def hangman():
    words = ["python", "design", "college", "project", "hangman"]
    word = words[0]  
    guessed = ["_"] * len(word)
    attempts = 6
    used_letters = []
    print("Welcome to Hangman!")
    print("Word to guess:", " ".join(guessed))
    while attempts > 0 and "_" in guessed:
        guess = input("Enter a letter: ").lower()
        if guess in used_letters:
            print("Already guessed that letter!")
            continue
        used_letters.append(guess)
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
            print("Correct guess!")
        else:
            attempts -= 1
            print("Wrong guess! Attempts left:", attempts)
        print("Word:", " ".join(guessed))
        print("Used letters:", ", ".join(used_letters))
    if "_" not in guessed:
        print("You won! The word was:", word)
    else:
        print("Game over! The word was:", word)
hangman()
