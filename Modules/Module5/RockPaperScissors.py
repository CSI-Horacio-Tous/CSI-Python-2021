def main ():

    playagain = 'y'

    while playagain == 'y' :

        Rock= 'Rock'
        Paper= 'Paper'
        Scissors= 'Scissors'


        moves=input('Rock , Paper , Scissors ? \n') 


        import random

        foo = [Rock , Paper , Scissors]
        computerChoice = random.choice(foo)
        print(f"Computer selected: {computerChoice}")

        if computerChoice == moves :
            print('Tie')


        # Rock
        if moves == Rock:
            
            

            if computerChoice == Paper :
                print ('Loser')

            if computerChoice == Scissors :
                print ('Winner')



        # Paper

        if moves == Paper:
            


            if computerChoice == Scissors :
                print ('Loser')

            if computerChoice == Rock :
                print ('Winner')



        # Scissors

        if moves == Scissors :
            
            
            if computerChoice == Rock:
                print ('Loser')

            if computerChoice == Paper :
                print ('Winner')

        playagain = input("Play again ? Enter 'y' for yes or 'n' for no \n" )
    print('Game concluded')
main()


