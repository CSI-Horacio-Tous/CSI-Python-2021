name = input('What is your name? \n')

print(f'Hello {name} ! Welcome to the Magic 8-Ball ')

question=input ('What do you want to ask me? \n')

print (f'{name} asks : {question}')

import random 

random_number = random.randint (1, 12)

if (random_number == 1 ):
    print('Yes - definitely.')

elif (random_number == 2 ):
    print('It is decidedly so.')

elif (random_number == 3 ):
    print('Without a doubt.')

elif (random_number == 4 ):
    print('Reply hazy, tray again.')

elif (random_number == 5 ):
    print('Reply hazy, tray again.')

elif (random_number == 6 ):
    print('Better not tell you now. ')

elif (random_number == 7 ):
    print('My sources say NO.')

elif (random_number == 8 ):
    print('Outlook not so good. ')

elif (random_number == 9 ):
    print('Very doubtful. ')

elif (random_number ==  10):
    print('Why would you ask that.')

elif (random_number == 11 ):
    print('Are you out of your mind to ask that.')

elif (random_number == 12 ):
    print('Figure out it yourself')

else:
    print('There was an error')
