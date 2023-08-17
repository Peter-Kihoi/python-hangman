import random
from stage import stages

word_list = ["aardvark", "baboon", "camel"]


def check_letter(word, guess_letter, display):
    for i, letter in enumerate(word):
        if guess_letter == letter:
            display[i] = guess_letter

    return display


def take_life(word, guess_letter, life):
    if guess_letter not in word:
        return life - 1
    return life - 0


def stage(life):
    return stages[life]


def check_full(display_list):
    return "_" not in display_list


def game(list_word):
    chosen_word = random.choice(list_word)
    display = []
    for _ in chosen_word:
        display.append("_")

    print(f"The word is {chosen_word}")
    life = 6
    guess_list = []
    game_on = True

    while game_on:
        guess = input("Guess a letter nigga: ")
        if guess in guess_list:
            print("You already guessed that. Guess Again")
        else:

            guess_list.append(guess)
            my_display = check_letter(chosen_word, guess, display)
            full = check_full(my_display)
            life = take_life(chosen_word, guess, life)
            hang = stage(life)

            if life <= 0:
                print(hang)
                print("You loose")
                return

            elif full:
                print(display)
                print("you win")
                return

            print(my_display)
            print(hang)


game(word_list)
