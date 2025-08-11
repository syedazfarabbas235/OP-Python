class Point:
    def __init__(self,x=0,y=0):
        self._x=x
        self._y=y
        if isinstance(x,Point):
            self._x= x._x
            self._y=x._y
        else:
            self._x=x
            self._y=y   

    @property
    def x(self):
        return self._x 
    @x.setter
    def x(self,value):
        self._x=value

    @property
    def y(self):
        return self._y
    @y.setter
    def y(self,value):
        self._y=value

    def add(self,other):
        return Point(self.x+other.x,self.y+other.y)
    def __add__(self,other) :
        return self.add(other) 
    
    def subtract(self,other):
        return Point(self.x-other.x,self.y-other.y)
    
    def __sub__(self,other) :
        return self.subtract(other)
    
    def distance(self,p):
        return((self.x-p.x)**2+(self.y-p.y)**2)**0.5
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def __repr__(self):
        return f"Point(x={self.x},y={self.y})"
    
    

            

