import random
word_list = ["Bayamon", "Aguadilla", "Rincon", "Patillas", "Arecibo", "Loiza", "Aguada",
"Cayey", "Jayuya", "Isabela" ]
def get_word(word_list):
    word=random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters= []
    guessed_words = []
    tries = 6
    print('A Jugar Hangman')
    print('Tema = Pueblos de Puerto Rico')
    print(display_hangman(tries))
    print(word_completion)
    [print("\n")]
    while not guessed and tries > 0:
        guess = input("Guess a letter or word").upper()
        if len(guess) == 1 and guess.isalpha():
            print("You already tried" , guess, "!")
        elif guess not in word:
            print("Isn't in the word : (")
            tries -= 1
            guessed_letters.append(guess)




def display_hangman(tries):
 stages = [ """
--------
 | |
 | O
 |/|\\
 | |
 | / \\
 -
 """,
 """
 --------
 | |
 | O
 |/|\\
 | |
 | /
 -
 """,
 """
 --------
 | |
 | O
 |/|\\
 | |
 |
 -
 """,
 """"
 --------
 | |
 | O
 |/|
 | |
 |
 -
 """,
 """
 --------
 | |
 | O
 | |
 | |
 |
 -
 """,
 """
 --------
 | |
 | O
 |
 |
 |
 -
 """,
 """
 --------
 | |
 |
 | 
 |
 |
 -
 """,
 ]