from geometry.point import Point
from drawing.pen import Pen
class Square:
    def __init__(self,start_point:Point,side_length=float):
        self.start_point=start_point
        self.side_length=side_length
    def draw_square(self,pen):   
        x=self.start_point.x
        y=self.start_point.y   
        side=self.side_length
        

        pen.move_to(x,y)            
        pen.line_to(x+side,y)
        pen.line_to(x+side,y+side)
        pen.line_to(x,y+side)
        pen.line_to(x,y)
