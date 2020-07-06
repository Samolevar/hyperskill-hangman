import random

# Write your code here
words = ['python', 'java', 'kotlin', 'javascript']
hidden_word = str(random.choice(words))
errors_count = 0
repeated_bad_letters = []


def replace_by_hyphens(string: str):
    for char in string:
        string = string.replace(char, '-')
    return string
# answer = input(f'Guess the word {hidden_word[:3]}{replace_by_hyphens(hidden_word[2:])}: ')


def play_game(errors: int):
    while errors < 8:
        print('\n' + ''.join(guess))
        if guess == hidden_word:
            print("You guessed the word!\nYou survived!")
            break
        letter = input(f'Input a letter: ')
        if len(letter) > 1:
            print("You should input a single letter")
            continue
        if not letter.isalpha() or not letter.islower():
            print("It is not an ASCII lowercase letter")
            continue
        if letter in guess or letter in repeated_bad_letters:
            print("You already typed this letter")
            continue
        if letter not in hidden_word:
            print("No such letter in the word")
            repeated_bad_letters.append(letter)
            errors += 1
            continue
        for i in range(len(hidden_word)):
            if hidden_word[i] == letter:
                guess[i] = letter
    else:
        print("You are hanged!")


guess = [letter for letter in replace_by_hyphens(hidden_word)]
print('H A N G M A N\n')
print('Type "play" to play the game, "exit" to quit:')
choose = input()
if choose == "play":
    play_game(errors_count)
