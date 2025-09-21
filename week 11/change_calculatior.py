class ChangeCalculator:
    """
    A simple change calculator for PKR.

    This class computes the change (notes and coins) to return when a
    customer gives more money than the amount charged.
    """

    def __init__(self, charged_amount:int=100, given_amount:int =100):
        """
        Attributes:
        - _charged (int): Amount charged.
        - _given (int): Amount given by the customer.
        - _currency_values (list[int]): Available PKR notes/coins.
        - _breakdown (dict): Stores denomination -> quantity.
        """
        if isinstance(charged_amount,ChangeCalculator):
            # Copy constructor: If first argument is a ChangeCalculator object
            self._charged_amount = charged_amount._charged_amount
            self._given_amount = charged_amount._given_amount
            self._currency_values = [5000, 1000, 500, 100, 50, 20, 10, 5, 2, 1]
            self._breakdown = {}

        else:    
            # Normal constructor: validate and assign charged & given
            self._validate_amounts(charged_amount, given_amount)
            self._charged_amount = charged_amount
            self._given_amount = given_amount
            # List of available notes/coins in PKR
            self._currency_values = [5000, 1000, 500, 100, 50, 20, 10, 5, 2, 1]
            self._breakdown = {}

        # 🔑 Automatically calculate change
        self.process()    

    # ---------- Properties ----------
    @property
    def charged_amount(self):
        """Getter for charged amount."""
        return self._charged_amount

    @charged_amount.setter
    def charged_amount(self, value):
        """Setter for charged amount (with validation)."""
        self._charged_amount =self._validate_amount(value)

    @property
    def given_amount(self):
        """Setter for given amount (with validation)."""
        return self._given_amount

    @given_amount.setter
    def given_amount(self, value):
        """Getter for breakdown dictionary (denomination -> count)."""
        self._given_amount = self._validate_amount(value)

    @property
    def breakdown(self):
        return self._breakdown

    # ---------- Validation ----------
    def _validate_amount(self, value):
        """
        Validate a single amount (must be int and non-negative).

        Raises:
        - TypeError if not int
        - ValueError if negative
        """

        if not isinstance(value, int):
            raise TypeError("Amount must be an integer (PKR).")
        if value < 0:
            raise ValueError("Amount cannot be negative.")

    def _validate_amounts(self, charged_amount, given_amount):
        """
        Validate both charged and given amounts.

        Ensures:
        - Both are valid integers
        - Given >= charged (otherwise change is impossible)
        """

        self._validate_amount(charged_amount)
        self._validate_amount(given_amount)
        if given_amount < charged_amount:
            raise ValueError("Given amount must be >= charged amount.")

    # ---------- Core behaviour ----------
    def process(self):
        """
        Compute the change breakdown.

        Steps: 
        1. Calculate remaining change = given - charged.
        2. Loop through all available currency values.
        3. For each value, calculate how many notes/coins fit.
        4. Subtract from remaining and update breakdown dictionary.
        """

        remaining_amount = self.given_amount-self.charged_amount

        for value in self._currency_values:
            if value <=remaining_amount:
                count = remaining_amount // value
                remaining_amount -= count * value
                self.breakdown[value] = count

        """
        Compute the change and store the number of each note/coin.

        Example:
        Suppose:
            charged = 430
            given   = 1000
            remaining_amount = 1000 - 430 = 570

        Steps:
        - Start with remaining_amount = 570
        - Check 5000 → 570//5000=.... too big, skip
        - Check 1000 → 570//1000=....too big, skip
        - Check 500  → 570 // 500 = 1 → take 1 note of 500
            remaining_amount = 570 - (1*500) = 70
        - Check 100  → 70 < 100, skip
        - Check 50   → 70 // 50 = 1 → take 1 note of 50
            remaining_amount = 70 - (1*50) = 20
        - Check 20   → 20 // 20 = 1 → take 1 note of 20
            remaining = 20 - (1*20) = 0
        - No more remaining → done

        Final breakdown:
            {500: 1, 50: 1, 20: 1}
        """




    # ---------- Display ----------
    def display(self):
        """
        Nicely print the change in a human-readable format.

        Shows:
        - Amount charged
        - Amount given
        - Total change
        - Breakdown of notes and coins
        """

        change_due = self.given_amount - self.charged_amount
        print(f"Amount charged: Rs. {self.charged_amount}")
        print(f"Amount given:   Rs. {self.given_amount}")
        print(f"Total change:   Rs. {change_due}\n")
        print("Breakdown:")
        for value, count in self.breakdown.items():
            if count:
                label = "note" if value >= 10 else "coin"
                print(f"{count} x Rs. {value} {label}(s)")
        print("-"*40,"\n")    

    # ---------- String representation ----------
   
    def __str__(self):
        result = f"Change due: Rs. {self.given_amount - self.charged_amount}\n"
        for value, count in self.breakdown.items():
            if count:
                result += f"{count} x Rs. {value}\n"
        return result.strip()
