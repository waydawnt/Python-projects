import random

print("Welcome to to Hangman Game!")

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']

word_list = ['naruto', 'barakamon', 'pokemon', 'pokemon', 'shinchan', 'doraemon', 'atashinchi', 'maruko']
chosen_word = random.choice(word_list)

print(f"The chosen word is {chosen_word}.")

#variable declaration
lives = 6
display = []
word_length = len(chosen_word)

#add '_' in display list equal to the length of 'chosen_word'
for _ in range(word_length) :
    display += "_"
print(display)

end_of_game = False
while not end_of_game :
    #Ask user to guess a letter included in the 'chosen_word'
    guess = input("Guess a letter : ").lower()

    if guess in display :
        print(f"You already typed the letter '{guess}'.")
    else :
        #if the letter at that position matches the 'guess' then reveal that letter in the display at that position
        for position in range(word_length) :
            letter = chosen_word[position]
            if letter == guess :
                display[position] = letter

        if guess not in chosen_word :
            lives -= 1
            if lives == 0 :
                end_of_game = True
                print("You Lose!")

        if "_" not in display :
            end_of_game = True
            print("You Win!")

        print(f"Lives : {lives}")
        print(stages[lives])
        print(f"".join(display))