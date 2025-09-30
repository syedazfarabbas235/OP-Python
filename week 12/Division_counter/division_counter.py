class DivisionCounter:
    """
    A class to count how many times a positive integer (> 2) 
    can be divided by 2 before the result becomes less than 2.
    """

    # ---------- Constructor ----------
    def __init__(self, value):
        # Copy constructor: if value is already a DivisionCounter, copy its internal value
        if isinstance(value, DivisionCounter):
            self._value = value._value
        else:
            # Validate the input before setting it
            self._validate_input(value)
            self._value = value

    # ---------- Property: value ----------
    @property
    def value(self):
        """Getter for the current value"""
        return self._value

    @value.setter
    def value(self, new_value):
        """Setter for the value with validation"""
        self._validate_input(new_value)
        self._value = new_value

    # ---------- Validation ----------
    def _validate_input(self, val):
        """
        Internal method to ensure the input is valid:
        - Must be an integer
        - Must be greater than 2
        Raises exceptions if invalid.
        """
        if not isinstance(val, int):
            raise TypeError("Input must be an integer")
        if val <= 2:
            raise ValueError("Input must be greater than 2")

    # ---------- Core Logic ----------
    @property
    def count_divisions(self):
        """
        Property: compute and return the number of times
        this value can be divided by 2 before becoming < 2.
        """
        n = self.value
        steps = 0
        while n >= 2:
            n = n / 2  # Divide by 2
            steps += 1  # Count each division
        return steps

    # ---------- Display ----------
    def display(self):
        """
        Prints a detailed report of the division process.
        Shows initial value and number of division steps.
        """
        print("📉 Division by 2 Process Report")
        print("=" * 40)
        print(f"Initial Value      : {self.value}")
        print(f"Steps to < 2       : {self.count_divisions}")
        print("=" * 40)

    # ---------- String Representation ----------
    def __str__(self):
        """
        Returns a concise string representation of the object.
        Useful for printing or debugging.
        """
        return f"Value: {self.value}, Steps: {self.count_divisions}"
