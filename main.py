import random


import hangman_words
word_list = hangman_words.word_list
lives = 6

import hangman_art
stages = hangman_art.stages
logo = hangman_art.logo
print(logo)

chosen_word = random.choice(word_list)

placeholder = ""
for character in chosen_word:
    placeholder += "_"
print("Word to guess: " + placeholder)



game_over = False
correct_letters = []

while not game_over:


    print(f"****************************<???>/{lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()


    display = ""
    if guess in correct_letters:
        print("You already guessed " + guess)
        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"
    else:
        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"

    print("Word to guess: " + display)

    
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

        if lives == 0:
            game_over = True

           
            print(f"The correct answer was {chosen_word}!. YOU LOSE!")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
