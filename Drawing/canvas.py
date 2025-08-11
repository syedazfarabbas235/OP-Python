import tkinter as tk
from geometry.point import Point  # Assuming you have a Point class defined in geometry module
from geometry.line import Line  # Your existing Point class



class Tpanel(tk.Canvas):
    def __init__(self, master=None, width=400, height=400, **kwargs):
        super().__init__(master, width=width, height=height, bg='white', **kwargs)
        self.lines = []

    def add_line(self, p1: Point, p2: Point):
        """Adds a line and triggers drawing"""
        self.lines.append(Line(p1, p2))
        print(f"Line from ({p1.x}, {p1.y}) to ({p2.x}, {p2.y})")
        self.draw()  # Mimic Java's repaint()

    def draw(self):
        """Draw all stored lines"""
        self.delete("all")  # Clear previous drawings
        for line in self.lines:
            self.create_line(line.start.x, line.start.y,
                             line.end.x, line.end.y,
                             fill='black', width=2)