from range import Range
def main():
    #forward printing
    r1=Range(3,9,1)
    print (r1)
# copy
    r2=Range(r1)   
    print(r2)
    #backward printing
    r3=Range(10,1,-1)
    print(r3)
#checking if the number is within the range or not
    is_in_range=(2 in r1)
    print(is_in_range)
    print(3 in r3)
main()