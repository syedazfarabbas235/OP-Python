import tkinter as tk
from geometry.point import Point
from shapes.triangle import Triangle
from drawing.pen import Pen
from shapes.square import Square

def main():
    root = tk.Tk()
    pen=Pen(root)
    

    triangle = Triangle(Point(50, 350),base=300,height=300)
    square= Square(Point(50,50),side_length=300)
    triangle.draw_triangle(pen) 
    square.draw_square(pen)  
    root.mainloop()

if __name__ == "__main__":
    main()
