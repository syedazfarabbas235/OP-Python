from math import gcd
class Rational:
    def __init__(self,numerator:int,denominator:int):
        if denominator==0:
            raise ValueError("Denominator cant be zero")
        
        self._numerator=numerator
        self._denominator=denominator
        self.reduce()

    @property
    def numerator(self):
        return self._numerator
    @numerator.setter
    def numerator(self,value):
        self._numerator=value

    @property
    def denominator(self):
        return self._denominator
    @denominator.setter
    def denominator(self,value):
        self._denominator=value
    

    def reduce(self):
        common_divisor= gcd(self.numerator,self.denominator)   
        self.numerator= int(self.numerator/common_divisor)
        self.denominator=int(self.denominator/common_divisor)

    def __add__(self,other): 
        new_numerator= self.numerator * other.denominator + other.numerator*self.denominator
        new_denominator= self.denominator * other.denominator
        return Rational(new_numerator,new_denominator)
    
    def __sub__(self,other):
        new_numerator= self.numerator * other.denominator - other.numerator*self.denominator
        new_denominator= self.denominator * other.denominator
        return Rational(new_numerator,new_denominator)
    
    def __mul__(self,other):
        new_numerator= self.numerator * other.numerator
        new_denominator= self.denominator * other.denominator
        return Rational(new_numerator,new_denominator)
    
    def __truediv__(self,other):
        if other.numerator==0:
            raise ValueError("cant divide by zero")
        new_numerator= self.numerator*other.denominator
        new_denominator= self.denominator*other.numerator
        return Rational(new_numerator,new_denominator)
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
