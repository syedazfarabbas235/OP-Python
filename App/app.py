from drawing.pen import Pen
from geometry.point import Point
from Turtle.turtle import turtle           # your custom Turtle class
from Turtle.commands import SquareCommand, ZigZagCommand

class App:
    def __init__(self, pen):
        # Initialize Pen and Turtle
        self.pen = pen
        self.turtle = turtle(self.pen, Point(150, 150),0)

        # List of commands to execute
        self.commands = [
            SquareCommand(),
            ZigZagCommand()
        ]

    def run(self):
        # Execute each command
        for command in self.commands:
            command.execute(self.turtle)

    def run_square_only(self):
        SquareCommand().execute(self.turtle)

    def run_zigzag_only(self):
        ZigZagCommand().execute(self.turtle)
