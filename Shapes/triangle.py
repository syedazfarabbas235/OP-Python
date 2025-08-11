from geometry.point import Point
from drawing.pen import Pen
class Triangle:
    def __init__(self,start_point:Point,base:float,height:float):
       self.start_point=start_point
       self.base=base
       self.height=height

    def draw_triangle(self, pen):  
        x=self.start_point.x
        y=self.start_point.y
        base=self.base
        height=self.height     
        pen.move_to(x,y)            
        pen.line_to(x+base,y)
        pen.line_to(x+base/2,y-height)
        pen.line_to(x,y)
