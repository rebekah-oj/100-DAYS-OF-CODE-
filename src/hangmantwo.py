import random
import hangmanart
import hangmanword

# word_list = ['ardwark', 'baboon', 'camel']
word_list = hangmanword.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6
print(hangmanart.logo)

print(f"Psst, the solution is {chosen_word}.")

display = []

for letter in range(word_length):
    display += "_"
    print(display)

end_of_game = False

letter = " "
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have previously entered this letter {letter}")

    for position in range(word_length):
        letter = chosen_word[position]

        print(f"Current position: {position}\n"
              f"current letter: {letter}\n"
              f"letter: {guess}")

        if letter == guess:
            display[position] = letter

        if guess not in chosen_word:
            print(f"letter is not in {chosen_word}")
            lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose. ")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangmanart.stages[lives])
