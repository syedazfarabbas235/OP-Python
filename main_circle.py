import tkinter as tk
from drawing.canvas import Tpanel
from geometry.point import Point
from shapes.circle import Circle

root = tk.Tk()
root.title("Canvas Example")

# Create drawing panel
panel = Tpanel(root, width=400, height=400)
panel.pack()

# Example: draw a line
p1 = Point(200,200 )
p2 = Point(100,200)
panel.add_line(p1, p2)

# Example: draw a circle
center_point = Point(200,200)
circle = Circle(center_point, 100)
print(f"Circle area: {circle.area():.2f}")

root.mainloop()
