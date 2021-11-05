# gun = "Glock 17"
# caliber = ' 9 X 19mm '
# ammunition= "PBP gzh"
# Velocity = 560

# Building = 'Caribbean Sea Views'
# Buildingheight = 334

# gravity= 9.8

import math
from ExperimentalData import ExperimentalData

def Projectilefunction(expermientalData: ExperimentalData):

    time_s = math.sqrt((2 * experimentalData.Buildingheight) / experimentalData.gravity) 

    distance_m =(experimentalDAta.Velocity * time_s)
    #distance_m =(experimentalData[Velocity] * time_s)


print(f'The gun selected for the experiment is {expermientalData.gun} and it uses {expermientalData.caliber} caliber with {expermientalData.ammunition} ammuniton.')

print(f'The gun with that ammunition has a projectile speed of {expermientalData.Velocity} ms')

print(f'The experiment will take place in {expermientalData.Building} that is {expermientalData.Buildingheight} ft tall.')

#convert your script parameters into a singles JSON Object

experimentalData= {

'gun': "Glock 17" ,
'caliber' : ' 9 X 19mm ',
'ammunition': 'PBP gzh', 
'Velocity' : 560 ,
'Building' : 'Caribbean Sea Views',
'Buildingheight' : 334 ,
'gravity': 9.8





}

experimentalData = ExperimentalData('Glock 17','9 X 19mm' , 'PBP gzh' , 560 , 334 ,'Caribbean Sea Views' , 'Caribbean Sea Views'

Projectilefunction