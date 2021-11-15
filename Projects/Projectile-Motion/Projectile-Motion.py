import math
import os
from pathlib import Path
from ExperimentalData import ExperimentalData
import json 

# gun = "Glock 17"
# caliber = ' 9 X 19mm '
# ammunition= "PBP gzh"
# Velocity = 560

# Building = 'Caribbean Sea Views'
# Buildingheight = 334

# gravity= 9.8



def Projectilefunction(experimentalData: ExperimentalData):

    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    g_ms2 = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]

    planet= planets.index(experimentalData.planet)


    time_s=math.sqrt((2 * experimentalData.Buildingheight) / g_ms2[planet] ) 

    distance_m = (experimentalData.Velocity * time_s)
    #distance_m =(experimentalData[Velocity] * time_s)


    print(f'The gun selected for the experiment is {experimentalData.gun} and it uses {experimentalData.caliber} caliber with {experimentalData.amunition} ammuniton.')

    print(f'The gun with that ammunition has a projectile speed of {experimentalData.Velocity} ms')

    print(f'The experiment will take place in {experimentalData.Building} that is {experimentalData.Buildingheight} ft tall.')

    print(f'The projectile will travel {distance_m} meters in {time_s} seconds in {experimentalData.planet}')
#convert your script parameters into a singles JSON Object

# experimentalData= {

# 'gun': "Glock 17" ,
# 'caliber' : ' 9 X 19mm ',
# 'ammunition': 'PBP gzh', 
# 'Velocity' : 560 ,
# 'Building' : 'Caribbean Sea Views',
# 'Buildingheight' : 334 ,
# 'gravity': 9.8





# }

# experimentalData = ExperimentalData('Glock 17','9 X 19mm' , 'PBP gzh' , 560 , 334 ,'Caribbean Sea Views' , 'Caribbean Sea Views')

myDataset = [

ExperimentalData("Glock 17","9 X 19mm" , "PBP gzh" , 560 , 334 ,"Caribbean Sea Views" , "Earth"),

ExperimentalData("Glock 17","9 X 19mm" , "AP 6.3" , 392 , 334 ,"Caribbean Sea Views" , "Mars"),

ExperimentalData("Glock 17","9 X 19mm" , "T gzh" , 365 , 334 ,"Caribbean Sea Views" , "Venus"),

ExperimentalData("Glock 17", "9 X 19mm" , "Luger CCI" , 420 , 334 ,"Caribbean Sea Views"  , "Saturn"),

ExperimentalData("Glock 17","9 X 19mm" , "PSO gzh" , 340 , 334 ,"Caribbean Sea Views" ,  "Mercury")

]
for data in myDataset:
    print("\n--------------------------------------------------\n")
    Projectilefunction(data)

myOutputPath= Path(__file__).parents[0]
myOutputPath = os.path.join (myOutputPath, 'Projectile-Motion.json')

print(myOutputPath)

with open(myOutputPath, 'w') as outfile:
    json.dump([data.__dict__ for data in myDataset], outfile)
