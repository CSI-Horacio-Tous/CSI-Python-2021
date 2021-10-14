planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus' , 'Neptune']
gms = [3.7 , 8.87 , 9.81 , 3.711 , 24.79 , 10.44 , 8.69 , 11.15]

print ('I can calculate your weihgt in any planet')
myweight = int(input('What is your wheight (in pounds) ?'))

myplanet = input (f'Select a planet: {planets} \n ')

def calculateweight (planet , mass):
    print(f'Earth mass in pounds is : {mass}')

    wkg = mass / 2.2046
    print(f'Mass in kg :{wkg}')

    nlb = 4.45 

    plantindex = planets.index(planet) 
    print (f'Your wheight in {planets[plantindex]} is {(wkg * gms[plantindex]) / nlb} lb.')

calculateweight(myplanet , myweight)

