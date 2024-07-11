def hangman():
    words = ["no", "bet", "bomb", "green", "jailed", "javelin", "projects", "elsewhere", "baptized"]
    
    play_or_not = input("Hello! Do you want to play hangman? (yes/no): ")
    if play_or_not == "no":
        print("Goodbye!")
        return
    
    word_count = int(input("Choose how many letters (2-10): "))
    selected_word = ""
    
    for item in words:
        if word_count == len(item):
            selected_word = item
            break
    
    if selected_word == "":
        print("No words found with the specified length.")
        return
    
    guessed_word = ["_"] * len(selected_word)
    attempts = 7
    guessed_letters = []
    
    print("Let's play Hangman!")
    print(" ".join(guessed_word))
    
    while attempts > 0:
        guess = input("Guess a letter: ")
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in selected_word:
            print("Good guess!")
            for i in range(len(selected_word)):
                if selected_word[i] == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print("Wrong guess! You have " + str(attempts) + " attempts left.")
        
        print(" ".join(guessed_word))
        
        if "_" not in guessed_word:
            print("Congratulations! You guessed the word correctly!")
            break
    else:
        print("You've run out of attempts! The word was '" + selected_word + "'.")

hangman()