# This is the hangman game


def hangman():
    word = input("What is your word? \n")
    length_word = len(word)
    theme = input("What is the theme of the word? \n")
    print_info(length_word, theme)
    wrong_guess = []
    right_guess = []
    letter = input("Guess a letter \n")
    if letter not in word:
        wrong_guess.append(letter)
        length_word -= 1
    else:
        right_guess.append(letter)

    print_info(length_word, theme)


def print_info(count, theme):
    print("Guesses left: ", count)
    print("The theme is: ", theme)
    counter = 0
    while counter <= count:
        counter += 1
        print("_ ", end="")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hangman()
