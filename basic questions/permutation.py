class PermutationGenerator:
    """
    A class to generate all possible strings formed 
    by using given characters exactly once.
    """

    # ---------- Constructor ----------
    def __init__(self, characters):
        # Copy constructor: if characters is already a PermutationGenerator, copy its internal characters
        if isinstance(characters, PermutationGenerator):
            self._characters = list(characters._characters)
        else:
            # Validate input and store characters as a list
            self._validate_input(characters)
            self._characters = list(characters)

        

    # ---------- Properties ----------
    @property
    def characters(self):
        """Getter for the characters as a list"""
        return list(self._characters)

    @characters.setter
    def characters(self, new_chars):
        """Setter for characters with validation"""
        self._validate_input(new_chars)
        self._characters = list(new_chars)

    # ---------- Validation ----------
    def _validate_input(self, chars):
        """
        Internal method to validate input.
        Ensures the input is a string.
        """
        if not isinstance(chars, str):
            raise TypeError("Input must be a string")

    # ---------- Core Logic ----------
    def _permute(self, current, remaining):
        """
        Recursive helper function to generate permutations.
        current   : string formed so far
        remaining : list of remaining characters
        """
        if len(remaining) == 0:
            # Base case: all characters used, add permutation to the list
            self._permutations.append(current)
            return

        # Recurse for each character in remaining
        for i in range(len(remaining)):
            # Build new remaining list excluding the current character
            new_remaining = [remaining[j] for j in range(len(remaining)) if j != i]
            # Recurse with updated current string and new remaining
            self._permute(current + remaining[i], new_remaining)

    @property
    def generate_permutations(self):
        """
        Public property to generate all permutations.
        Resets previous permutations before generating new ones.
        Returns a copy of the list of permutations.
        """
        self._permutations = []
        self._permute("", self._characters)
        return self._permutations

    # ---------- Display ----------
    def display(self):
        """
        Prints all generated permutations in a formatted manner.
        Shows total number of permutations at the end.
        """
        print("🔠 All Possible Strings:")
        perms = self.generate_permutations
        for word in perms:
            print(word)
        print("Total permutations:", len(perms))
        print("-" * 30)

    # ---------- String Representation ----------
    def __str__(self):
        """
        Returns a concise string representation of the object.
        Useful for debugging or printing.
        """
        return f"Characters: {''.join(self.characters)}, Total permutations: {len(self.generate_permutations)}"
