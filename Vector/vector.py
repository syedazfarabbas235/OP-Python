import math

class Vector:
    def __init__(self, d=1): # default constructor
        """Create vector from dimension (zeros) or from list of values"""
        if isinstance(d, Vector):  # copy constructor
            self._coords = list(d._coords)
        elif isinstance(d,int):
            self._coords= [0]*d
        else:
            raise TypeError("Vector must be created with int (dimension) values.")

    # ---------------- Properties ---------------- #

    @property
    def coords(self):
        #Get the list of coordinates
        return self._coords

    @coords.setter
    def coords(self, values):
        #Set the entire coordinates list
        if len(values) != len(self._coords):
            raise ValueError("New values must match vector dimension")
        self._coords = list(values) # store all given values as a new list in _coords

    def __len__(self):
        """Number of dimensions"""
        return len(self._coords)

    # ---------------- Arithmetic Operations ---------------- #

    def __add__(self, other):
        #adding vectors
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result._coords[j] = self._coords[j] + other._coords[j]
        return result

    def __sub__(self, other):
        #subtracting vectors
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result._coords[j] = self._coords[j] - other._coords[j]
        return result

    def __eq__(self, other):
        # equality: two vectors are equal if all their coordinates are the same
        return self._coords == other._coords

    def __ne__(self, other):
        # inequality: two vectors are not equal if they differ in any coordinate
        return not self == other

    def __str__(self):
        return '(' + str(self._coords)[1:-1] + ')'  # convert coords list to string without [ ] and wrap in < >
    
    def __repr__(self):
        return f" (i,j,k) ({self.coords})"

    # ---------------- Extra Methods ---------------- #

    def dot_product(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = 0   # will hold the sum of products
        for j in range(len(self)):
            result += self._coords[j] * other._coords[j]   # multiply corresponding coordinates and add to resultbnm
        return result

    def magnitude(self):
        total = 0
        for j in range(len(self)):
            total += self.coords[j]**2   # square each coordinate and add
        return total**0.5   # square root using power operator


    def distance_to(self, other):
       # Calculating the distance between two vectors.
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        total = 0  # sum of squared differences
        """ calculate squared difference for each coordinate"""
        for j in range(len(self)):
            diff = self._coords[j] - other._coords[j] # difference between corresponding coords
            total += diff * diff # add square of the difference
        return total**0.5
