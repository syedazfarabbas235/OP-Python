from drawing.canvas import Tpanel
from geometry.point import Point
class Pen:
    def __init__(self,master=None):
        self._canvas=Tpanel(master)
        self._canvas.pack()
        self._cp=Point(0,0)


    def move_to(self,x,y):
        self._cp=Point(x,y)

    def line_to(self,x,y) :
        new_point=Point(x,y)   
        self._canvas.add_line(self._cp,new_point)
        self._cp=new_point
