class ChangeCalculator:
    """
    A simple change calculator for PKR using LIST of LISTS.
    """

    def __init__(self, charged_amount: int = 100, given_amount: int = 100):
        if isinstance(charged_amount, ChangeCalculator):
            # Copy constructor
            self._charged_amount = charged_amount._charged_amount
            self._given_amount = charged_amount._given_amount
            self._currency_values = [5000, 1000, 500, 100, 50, 20, 10, 5, 2, 1]
            self._breakdown = []
        else:
            # Normal constructor
            self._validate_amounts(charged_amount, given_amount)
            self._charged_amount = charged_amount
            self._given_amount = given_amount
            self._currency_values = [5000, 1000, 500, 100, 50, 20, 10, 5, 2, 1]
            self._breakdown = []

        self.process()

    # ---------- Properties ----------
    @property
    def charged_amount(self):
        return self._charged_amount

    @charged_amount.setter
    def charged_amount(self, value):
        self._charged_amount = self._validate_amount(value)

    @property
    def given_amount(self):
        return self._given_amount

    @given_amount.setter
    def given_amount(self, value):
        self._given_amount = self._validate_amount(value)

    @property
    def breakdown(self):
        return self._breakdown

    # ---------- Validation ----------
    def _validate_amount(self, value):
        if not isinstance(value, int):
            raise TypeError("Amount must be an integer (PKR).")
        if value < 0:
            raise ValueError("Amount cannot be negative.")
        return value

    def _validate_amounts(self, charged_amount, given_amount):
        self._validate_amount(charged_amount)
        self._validate_amount(given_amount)
        if given_amount < charged_amount:
            raise ValueError("Given amount must be >= charged amount.")

    # ---------- Core behaviour ----------
    def process(self):
        remaining_amount = self.given_amount - self.charged_amount
        self._breakdown = []  # reset list

        for value in self._currency_values:
            if value <= remaining_amount:
                count = remaining_amount // value
                remaining_amount -= count * value
                self._breakdown.append([value, count])  # 👈 inner list

    # ---------- Display ----------
    def display(self):
        change_due = self.given_amount - self.charged_amount
        print(f"Amount charged: Rs. {self.charged_amount}")
        print(f"Amount given:   Rs. {self.given_amount}")
        print(f"Total change:   Rs. {change_due}\n")
        print("Breakdown:")
        for value, count in self.breakdown:
            if count:
                label = "note" if value >= 10 else "coin"
                print(f"{count} x Rs. {value} {label}(s)")
        print("-" * 40, "\n")

    # ---------- String representation ----------
    def __str__(self):
        result = f"Change due: Rs. {self.given_amount - self.charged_amount}\n"
        for value, count in self.breakdown:
            if count:
                result += f"{count} x Rs. {value}\n"
        return result.strip()
