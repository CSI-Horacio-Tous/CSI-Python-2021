# gun = "Glock 17"
# caliber = ' 9 X 19mm '
# ammunition= "PBP gzh"
# Velocity = 560

# Building = 'Caribbean Sea Views'
# Buildingheight = 334

# gravity= 9.8

import math

# time_s = math.sqrt((2 * Buildingheight) / gravity) 

def Projectilefunction(gun:str , caliber:str , amunition:str , Velocity:int ,Buildingheight:int , Building:str , gravity:int )


print(f'The gun selected for the experiment is {gun} and it uses {caliber} caliber with {ammunition} ammuniton.')

print(f'The gun with that ammunition has a projectile speed of {Velocity} ms')

print(f'The experiment will take place in {Building} that is {Buildingheight} ft tall.')

Projectilefunction('Glock 17','9 X 19mm' , 'PBP gzh' , 560 , 334 ,'Caribbean Sea Views' , 'Caribbean Sea Views'