print("Welcomr to Simpsons'Shipping")

weight:float =float(input('What is the weight of your package:\n'))

#Ground

if (weight == 2 or weight < 2):
    costground= weight * 1.75 + 20

    print('Ground Shipping : $ ' ,float (costground))

elif (weight > 2  or weight <= 6 ):
    costground= weight * 3.50 + 20

    print('Ground Shipping : $ ' ,float (costground))

elif (weight > 6  or weight <= 10 ):
    costground= weight * 4.50 + 20

    print('Ground Shipping : $ ' ,float (costground))

else:
    costground = weight * 5.25 + 20

    print('Ground Shipping : $ ' ,float (costground))


#Courier

if (weight == 2 or weight < 2):
    courier= weight * 3.50 + 5

    print('Courier Shipping : $ ' ,float (courier))

elif (weight > 2  or weight <= 6 ):
    courier= weight * 7.00 + 8

    print('Courier Shipping : $ ' ,float (courier))

elif (weight > 6  or weight <= 10 ):
    courier= weight * 9.00 + 12

    print('Courier Shipping : $ ' ,float (courier))

else:
    courier = weight * 10.50 + 15

    print('Courier Shipping : $ ' ,float (courier))


#Drone

if (weight == 2 or weight < 2):
    drone= weight * 5.25

    print('Drone Shipping : $ ' ,float (drone))

elif (weight > 2  or weight <= 6 ):
    drone= weight * 10.50 

    print('Drone Shipping : $ ' ,float (drone))

elif (weight > 6  or weight <= 10 ):
    drone= weight * 13.50 

    print('Drone Shipping : $ ' ,float (drone))

else:
    drone = weight * 15.75

    print('Drone Shipping : $ ' ,float (drone))

#prime

print('$150')