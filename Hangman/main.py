# DAY 7

## Task Hangman Start
import random
import hangman_words
import hangman_art

stages = hangman_art.stages
words = hangman_words.word_list
stop = False
chosen_word = words[round(random.random() * (len(words) - 1))]
print(chosen_word)
blanks = []

lives = 6

for i in chosen_word:
    blanks.append("_")

print(hangman_art.logo)
while stop == False:
    guess = input("Guess the letter: ").lower()
    x = 0

    if guess in blanks:
        print("You've already guessed")
    elif guess == "stop":
        stop = True
    elif guess in chosen_word:
        for i in chosen_word:
            if guess == i:
                blanks[x] = guess
            x += 1
        print(blanks)
    else:
        print("----------\n")
        print(stages[lives - 1])
        print("\n----------")
        lives -= 1
        if lives == 0:
            print("Game over!")
            stop = True

    if "_" not in blanks:
        stop = True
        print("You win!!!")
        print(chosen_word)