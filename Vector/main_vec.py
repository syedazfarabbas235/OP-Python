from Vector import Vector
def main():
     # Create two vectors of dimension 3
    v1 = Vector(3)
    v2 = Vector(3)
    
    # Set coordinates for each vector
    v1.coords = [1, 2, 3]
    v2.coords = [4, 5, 6]
    print(v1)
    #setting new values
    v1.coords[0]=2
    
    # Perform vector addition
    v3 = v1 + v2

    print (v3)

    #Copy constructor
    v4= Vector(v3)
    print(v4)
    
    #Calculating distance
    distance=v1.distance_to(v2)
    print (distance)\
    
    #Checking if they are equal
    print(v1==v2)

main()    