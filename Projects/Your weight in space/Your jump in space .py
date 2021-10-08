planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus' , 'Neptune']
grav= [2.65 , 1.11 , 1 , 2.64 , 0.40 , 0.94 , 1.13 , 0.88]


print('Jumping on other planets') 

myjump=input('What is your jumps length on Earth (meters) ? ')

myplanet = input (f'Select a planet: {planets} \n ')

print(f'Your jump in earth is {myjump}')

def calculateweight (planets , grav):


    plantindex = planets.index(planets) 
    print (f'Your jump in {planets[plantindex]} is {(grav * planets[plantindex])} m.')


calculateweight(myplanet , myjump)


