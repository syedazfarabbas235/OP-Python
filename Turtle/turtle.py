import math
from geometry.point import Point
from drawing.pen import Pen

class turtle:
    def __init__(self,pen,current_pos=Point,angle=0, distance=100):   # default distance = 50 pixels
        self._pen=pen
        self._distance = distance
        self._current_pos=current_pos
        self._angle = angle  # facing right (0°)
        """
        Constructor for Turtle class

        Parameters:
        - pen: Pen object used for drawing on canvas
        - current_pos: Current position of the turtle (Point object)
        - angle: Current direction turtle is facing (in degrees)
                 (default = 0°, i.e., facing right along x-axis)
        - distance: How far the turtle moves forward each step (default = 50 pixels)
        """

     # Properties (safe access methods)
    @property
    def pen(self):
        """Read-only access to the Pen (composition)."""
        return self._pen
    
    @property
    def current_pos(self):
        """Read-only access to current position"""
        return self._current_pos
    
    @current_pos.setter
    def current_pos(self, value):
      if not isinstance(value, Point):
        raise TypeError("current_pos must be a Point")
      self._current_pos = value

    @property
    def angle(self):
        """Read-only access to angle"""
        return self._angle
    
    @angle.setter
    def angle(self, value):
        self._angle = value

    @property
    def distance(self):
        """Get or set distance (with validation)"""
        return self._distance

    @distance.setter
    def distance(self, value):
        if value <= 0:
            raise ValueError("Distance must be positive.")
        self._distance = value    

        
    def move_forward(self):
        """
         Moves the turtle forward by 'distance' in the current 'angle' direction.
         Also draws a line from the current position to the new position.

          We want the next point after moving forward a certain distance in the direction we’re facing.
           Imagine you are standing on graph paper at (x, y) with a ruler.
           Your distance is how many steps you’ll take.
           Your angle tells which way you are facing (right, left, up, down).
           After moving, you land at a new point (new_x, new_y)"""
        
        # Current coordinates (starting point)
        x=self.current_pos.x
        y=self.current_pos.y

        # Place the pen at the starting position
        self.pen.move_to(self.current_pos.x, self.current_pos.y)

        # Convert angle from degrees → radians (needed for math functions)
        rad = math.radians(self.angle)
        """ rad = math.radians(self.angle)
          → Convert angle from degrees (like 0°, 90°) into radians (needed for Python’s math functions)."""

        # Calculate new x, y coordinates using trigonometr
        new_x = self.current_pos.x + self.distance * math.cos(rad)
        """ new_x = self.current_point.x + self.distance * math.cos(rad)
          → Start from the current x. Add the horizontal movement (distance × cos)."""
        
        new_y = self.current_pos.y + self.distance * math.sin(rad)
        """  new_y = self.current_point.y + self.distance * math.sin(rad)
          → Start from the current y. Add the vertical movement (distance × sin)."""

        # Create a Point object for the new position
        new_pos = Point(new_x, new_y)
        """  new_point = Point(new_x, new_y)
        → Bundle the new coordinates into a Point"""

      

        # Draw line from old point to new point
        self.pen.line_to(new_pos.x, new_pos.y)

        # Update turtle's current position
        self.current_pos = new_pos

    def turn_right(self):
        """
        Turns the turtle 90° clockwise.
        Example: right → down → left → up
        """
        self.angle += 90

    def turn_left(self):
        """
        Turns the turtle 90° counterclockwise.
        Example: right → up → left → down
        """
        self.angle -= 90
            
