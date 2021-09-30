Rock= 'Rock'
Paper= 'Paper'
Scissors= 'Scissors'


moves=input('Rock , Paper , Scissors ?')

import random

foo = [Rock , Paper , Scissors]
computerChoice = random.choice(foo)
print(f"Computer selected: {computerChoice}")


# Rock
if moves == Rock:
    
    if computerChoice == Rock :
     print ('Tie')

    if computerChoice == Paper :
     print ('Loser')

    if computerChoice == Scissors :
     print ('Winner')


# Paper

if moves == Paper:
    
    if computerChoice == Paper :
     print ('Tie')

    if computerChoice == Scissors :
     print ('Loser')

    if computerChoice == Rock :
     print ('Winner')

# Scissors

if moves == Scissors :
    
    if computerChoice == Scissors :
     print ('Tie')

    if computerChoice == Rock:
     print ('Loser')

    if computerChoice == Paper :
     print ('Winner')


