import random
word_list = ["Bayamon", "Aguadilla", "Rincon", "Patillas", "Arecibo", "Loiza", "Aguada",
"Cayey", "Jayuya", "Isabela" ]
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