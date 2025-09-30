class ChangeCalculator:
    """
    A simple change calculator for PKR
    Demonstrates LIST, DICTIONARY, and STATIC ARRAY breakdowns.
    Also shows that Python does NOT support true function overloading.
    """

    def __init__(self, charged_amount=100, given_amount=100):
        self._charged_amount = charged_amount
        self._given_amount = given_amount
        self._currency_values = [5000, 1000, 500, 100, 50, 20, 10, 5, 2, 1]

        # storage styles
        self._list_breakdown = []                      
        self._dict_breakdown = {}                      
        self._static_breakdown = [[val, 0] for val in self._currency_values]  

        # try to "auto-process" all (but only last survives)
        self.process  

    # ---------------- Properties (results) ----------------
    @property
    def list_breakdown(self):
        return self._list_breakdown

    @property
    def dict_breakdown(self):
        return self._dict_breakdown

    @property
    def static_breakdown(self):
        return self._static_breakdown

    # ---------------- Attempted function overloading ----------------
    @property
    def process(self):
        """Dynamic List version"""
        print("LIST version running...")
        remaining = self._given_amount - self._charged_amount
        self._list_breakdown = []
        for val in self._currency_values:
            if val <= remaining:
                count = remaining // val
                remaining -= count * val
                self._list_breakdown.append([val, count])

    @property
    def process(self):
        """Dictionary version"""
        print("DICT version running...")
        remaining = self._given_amount - self._charged_amount
        self._dict_breakdown = {}
        for val in self._currency_values:
            if val <= remaining:
                count = remaining // val
                remaining -= count * val
                self._dict_breakdown[val] = count

    @property
    def process(self):
        """Static array version"""
        print("STATIC version running...")
        remaining = self._given_amount - self._charged_amount
        self._static_breakdown = [[val, 0] for val in self._currency_values]
        for i in range(len(self._currency_values)):
            val = self._currency_values[i]
            if val <= remaining:
                count = remaining // val
                remaining -= count * val
                self._static_breakdown[i][1] = count

    # ---------------- Display ----------------
    def display(self):
        print(f"Amount charged: Rs. {self._charged_amount}")
        print(f"Amount given:   Rs. {self._given_amount}")
        print(f"Total change:   Rs. {self._given_amount - self._charged_amount}\n")

        print("Breakdown (List):")
        for val, count in self._list_breakdown:
            if count:
                label = "note" if val >= 10 else "coin"
                print(f"{count} x Rs. {val} {label}(s)")
        print()

        print("Breakdown (Dict):")
        for val, count in self._dict_breakdown.items():
            if count:
                label = "note" if val >= 10 else "coin"
                print(f"{count} x Rs. {val} {label}(s)")
        print()

        print("Breakdown (Static Array):")
        for val, count in self._static_breakdown:
            if count:
                label = "note" if val >= 10 else "coin"
                print(f"{count} x Rs. {val} {label}(s)")
        print("-" * 40)
