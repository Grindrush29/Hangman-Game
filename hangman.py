import random
import hangman_words
import hangman_art
lives = 6
from hangman_art import logo
print(logo)

# randomizes word to be guessedimport hng
chosen_word = random.choice(hangman_words.word_list)
word_in_list = list(chosen_word)
print(f"Psst, the solution is {chosen_word}")

#Step 2
display = []
for _ in range(len(chosen_word)):
  display += "_"
string_v = " ".join(display)
print(string_v)

end_of_game = False
print(hangman_art.stages[6])

# Benginning of hangman
while end_of_game is False:
  guess = input("Guess a letter: ").lower()
# if the letter guessed is not in the word or has already been chosen 1 live taken
  if (guess not in chosen_word) or (guess in display):
    print(string_v)
    print()
    if guess not in chosen_word:
      print(f" The letter '{guess}' is not in chosen word")
    if guess in display:
      print(f"The letter '{guess}' has already been chosen")
    print(hangman_art.stages[lives-1])
    lives -= 1

# if letter guessed is in word and has not been chosen before show the letter
  elif guess in chosen_word:
    for i in range(len(chosen_word)):
      if guess == chosen_word[i]:
        display[i] = guess
        string_v = " ".join(display)
    print(string_v)
    print(hangman_art.stages[lives])

# win or lose conditions
  if lives == 0:
    end_of_game = True
    print("You lose")
  if display == word_in_list:
    end_of_game = True
    print("You win")