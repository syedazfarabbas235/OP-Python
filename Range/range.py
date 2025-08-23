class Range:
    """Custom implementation of Python's built-in range."""

    def __init__(self, start, stop=None, step=1):
        """
        Create a Range object.
        - start: beginning of the sequence
        - stop: one past the last value (not included)
        - step: increment (cannot be 0)

        """
        if isinstance(start,Range):
            #copy constructor
            self._start=start._start
            self._step=start._step
            self._length=start._length
            self.stop=start._stop
        


        else:    
         self._start = start
         self._step = step
         self._stop=stop
        
         if step == 0:
            raise ValueError("step cannot be 0")  # step must move forward or backward

         if stop is None:        # if only one argument is given → treat as range(0, start)
           # User called Range(n), meaning start should be 0 and stop should be n
          stop = start   # move the given number into stop
          start = 0      # reset start to 0


                

        # length calculation (handle positive and negative steps) 
         if step > 0:
                self._length = max(0, (stop - start + step - 1) // step)
         else:
                self._length = max(0, (stop - start + step + 1) // step)
    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        self._start = value
        if self._step > 0:
            self._length = max(0, (self._stop - self._start + self._step - 1) // self._step)
        else:
            self._length = max(0, (self._stop - self._start + self._step + 1) // self._step)

    @property
    def step(self):
        return self._step

    @step.setter
    def step(self, value):
        if value == 0:
            raise ValueError("step cannot be 0")
        self._step = value
        if self._step > 0:
            self._length = max(0, (self._stop - self._start + self._step - 1) // self._step)
        else:
            self._length = max(0, (self._stop - self._start + self._step + 1) // self._step)


    @property
    def length(self):
        return self._length
  

    def __len__(self):
        """Return how many numbers are in this range."""
        return self.length

    def __getitem__(self, index):
        """Return the k-th element (supports negative indices like lists)."""
        if index < 0:
            index += len(self)   # turn negative index into positive

        if not 0 <= index < self.length:   # make sure index is within valid range
            raise IndexError("index out of range")

        # formula for k-th term: start + (k * step)
        return self.start + index * self.step
    
    def __contains__(self, value):
     """Check if a value exists in the range."""
     if self.length == 0:   # empty range → no values
        return False

     last_value = self.start + (self.length - 1) * self.step 
     #Range(2, 10, 2) → start=2, step=2, length=4 → last = 2 + (3*2) = 8 So valid values are [2, 4, 6, 8].

    # check if value is between start and last_value (inclusive)
     if self._step > 0:
        if value < self.start or value > last_value:
            return False
     else:
        if value > self.start or value < last_value:
            return False

    # finally, check alignment with step
     return (value - self.start) % self.step == 0

    def __str__(self):
        """Show range as a simple list of numbers."""
        return str([self[i] for i in range(len(self))])
