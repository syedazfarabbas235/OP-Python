from abc import ABC, abstractmethod
from Turtle.turtle import turtle   # import Turtle class

class Command(ABC):
    @abstractmethod
    def get_pattern(self) -> str:
        """Return the command pattern as a string (F, +, -)"""
        pass

    def execute(self, turtle: turtle):
        """Interpret a string of commands (F, +, -) and send to Turtle"""
        pattern = self.get_pattern()
        for c in pattern:
            if c == "F":
                turtle.move_forward()
            elif c == "+":
                turtle.turn_right()
            elif c == "-":
                turtle.turn_left()


class SquareCommand(Command):
    def get_pattern(self) -> str:
        # F + → draw a side then turn right, repeated 4 times
        return "F+F+F+F+"


class ZigZagCommand(Command):
    def get_pattern(self) -> str:
        # Simple zigzag pattern
        return "F-F+F-F"
