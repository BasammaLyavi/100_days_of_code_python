import random

from hangman_word import word_list
from hangman_art import stages,logo

lives=6

print(logo)

chosen_word=random.choice(word_list)
print(chosen_word)

placeholder=''
word_length=len(chosen_word)
for position in range(word_length):
    placeholder+='_'
print("word to guess:"+placeholder)

game_over=False
correct_letters=[]
while not game_over:

    print(f"**************************{lives}/6 LIVERS LEFT********************************")
    guess=input("Guess a letter:").lower()

    if guess in correct_letters:
        print(f"yiu have already guessed{guess}")

    display = ''

    for letter in chosen_word:
        if letter==guess:
            display+=letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter
        else:
            display+="_"
    print("word to Guess:"+display)

    if guess not in chosen_word:
        lives-=1
        print(f"you guessed{guess},that's not in the word.you lose a life😒,")

        if lives==0:
            game_over=True
            print(f"**********************IT WAS {chosen_word} !*********************")

    if "_" not in display:
        game_over=True
        print("***********************YOU WIN THE GAME🏆***********************")

    print(stages[lives])
