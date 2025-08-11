import math
from geometry.point import Point

class Circle:
    def __init__(self, center: Point, radius: float):
        """Create a circle with center point and radius"""
        self.center = center
        self.radius = radius

    def area(self):
        """Return the area of the circle"""
        return math.pi * (self.radius ** 2)

    def draw2(self, canvas):
        """Draw the circle on a Tkinter Canvas"""
        x = self.center.x
        y = self.center.y
        r = self.radius
        canvas.create_oval(x - r, y - r, x + r, y + r,
                           outline='blue', width=2)
