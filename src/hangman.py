import random

word_list = ['ardwark', 'baboon', 'camel']

chosen_word = random.choice(word_list)

print(chosen_word)

guess = input("Guess a letter: ").lower()

# Check if the letter the
# user guessed (guess) is one of the letters in the chosen_word.
"""
for letter in chosen_word:
    print("Right")
else:
  print("Wrong")
"""
for letter in chosen_word:
    if letter == guess:
        print("Right")
else:
    print("wrong")
