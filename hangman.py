# This is the hangman game


def hangman():
    word = input("What is your word? \n")
    length_word = len(word)
    theme = input("What is the theme of the word? \n")
    print("Guesses left: ", length_word)
    print("The theme is: ", theme)
    counter = 0
    underscore = []
    if len(underscore) == 0:
        while counter <= length_word - 1:
            underscore.append("_")
            counter += 1
        counter = 0

    for j in underscore:
        print(j, " ", end="")
    wrong_guess = []
    right_guess = []
    indicies = []
    wrong_guesses = 0

    while wrong_guesses != len(word) - 1:
        print("If you want to guess the word press 1!")
        letter = input("Guess a letter \n")
        if letter == "1":
            guess_word = input("What is the word you want to guess: ")
            if guess_word == word:
                print("You Win, Congratulations Joyce/Igli!!!!!")
                exit(0)
            else:
                print("That is not correct! \n")
                wrong_guesses += 1
                length_word -= 1
                print_info(word, length_word, theme, letter, indicies, underscore)

                continue



        if letter not in word:
            print("Incorrect: ")
            wrong_guess.append(letter)
            wrong_guesses += 1
            length_word -= 1
            for i in wrong_guess:
                print(i, end=" ")
            print("\n")

        else:
            print("Correct!")
            right_guess.append(letter)
            i = 0
            while i <= len(word) - 1:
                if letter == word[i]:
                    indicies.append(i)
                    i += 1
                else:
                    i += 1

        print_info(word, length_word, theme, letter, indicies, underscore)
        indicies.clear()


def print_info(word, count, theme, letter, indices, placemats):
    print("Guesses left: ", count)
    print("The theme is: ", theme)
    i = 0

    while i <= len(word) - 1:
        if i in indices:
            placemats[i] = letter
            i += 1
        else:
            i += 1

    for k in placemats:
        print(k, " ", end=" ")

    print("If you want to guess the word press 1!")
    if letter == "1":
        guess_word = input("What is the word you want to guess: ")
        if guess_word == word:
            print("You Win, Congratulations Joyce/Igli!!!!!")
            exit(0)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hangman()
