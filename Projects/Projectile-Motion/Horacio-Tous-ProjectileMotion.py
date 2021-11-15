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

    time_s=math.sqrt((2 * experimentalData.Buildingheight) / experimentalData.gravity) 

    distance_m =(experimentalData.Velocity * time_s)
    #distance_m =(experimentalData[Velocity] * time_s)


    print(f'The gun selected for the experiment is {experimentalData.gun} and it uses {experimentalData.caliber} caliber with {experimentalData.ammunition} ammuniton.')

    print(f'The gun with that ammunition has a projectile speed of {experimentalData.Velocity} ms')

    print(f'The experiment will take place in {experimentalData.Building} that is {experimentalData.Buildingheight} ft tall.')

    print(f'The projectile will travel {distance_m} meters in {time_s} seconds')
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

ExperimentalData('Glock 17','9 X 19mm' , 'PBP gzh' , 560 , 334 ,'Caribbean Sea Views' , 'Caribbean Sea Views'),

ExperimentalData('Glock 17','9 X 19mm' , 'AP 6.3' , 392 , 334 ,'Caribbean Sea Views' , 'Caribbean Sea Views'),

ExperimentalData('Glock 17','9 X 19mm' , 'T gzh' , 365 , 334 ,'Caribbean Sea Views' , 'Caribbean Sea Views'),

ExperimentalData('Glock 17','9 X 19mm' , 'Luger CCI' , 420 , 334 ,'Caribbean Sea Views' , 'Caribbean Sea Views'),

ExperimentalData('Glock 17','9 X 19mm' , 'PSO gzh' , 340 , 334 ,'Caribbean Sea Views' , 'Caribbean Sea Views')

]
for data in myDataset:
    print("\n--------------------------------------------------\n")
    Projectilefunction(data)

myOutputPath= Path(__file__).parents[0]
myOutputPath = os.path.join (myOutputPath, 'Projectile-Motion-json')

print(myOutputPath)

with open(myOutputPath, 'w') as outfile:
    json.dump([__dict__ for data in myDataset], outfile)
