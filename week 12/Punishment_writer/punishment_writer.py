import random

class LinePunishmentWriter:
    """
    A class to write a punishment sentence multiple times with random typos.

    Attributes:
        _sentence (str): The original sentence to repeat.
        _repetitions (int): Number of times to repeat the sentence.
        _typo_count (int): Number of random typos per sentence.
    """

    # ---------- Constructor ----------
    def __init__(self, sentence: str, repetitions: int = 100, typo_count: int = 8):
        """
        Initializes the object with a sentence, repetition count, and typo count.

        Supports copy-constructor behavior if another LinePunishmentWriter is passed.
        """
        if isinstance(sentence, LinePunishmentWriter):
            # Copy constructor: duplicate attributes from existing object
            self._sentence = sentence._sentence
            self._repetitions = sentence._repetitions
            self._typo_count = sentence._typo_count
        else:
            # Validate input before storing
            self._validate_input(sentence, repetitions, typo_count)
            self._sentence = sentence
            self._repetitions = repetitions
            self._typo_count = typo_count

    # ---------- Properties ----------
    @property
    def sentence(self):
        """Getter for the sentence."""
        return self._sentence

    @sentence.setter
    def sentence(self, new_sentence):
        """Setter for sentence with validation."""
        self._validate_input(new_sentence, self._repetitions, self._typo_count)
        self._sentence = new_sentence

    @property
    def repetitions(self):
        """Getter for repetition count."""
        return self._repetitions

    @repetitions.setter
    def repetitions(self, new_reps):
        """Setter for repetition count with validation."""
        self._validate_input(self._sentence, new_reps, self._typo_count)
        self._repetitions = new_reps

    @property
    def typo_count(self):
        """Getter for typo count."""
        return self._typo_count

    @typo_count.setter
    def typo_count(self, new_typos):
        """Setter for typo count with validation."""
        self._validate_input(self._sentence, self._repetitions, new_typos)
        self._typo_count = new_typos

    # ---------- Validation ----------
    def _validate_input(self, sentence, repetitions, typo_count):
        """
        Internal method to validate input values.

        Raises:
            TypeError: If sentence is not a string.
            ValueError: If repetitions <= 0 or typo_count < 0.
        """
        if not isinstance(sentence, str):
            raise TypeError("Sentence must be a string")
        if not isinstance(repetitions, int) or repetitions <= 0:
            raise ValueError("Repetitions must be a positive integer")
        if not isinstance(typo_count, int) or typo_count < 0:
            raise ValueError("Typo count must be a non-negative integer")

    # ---------- Core Logic ----------
    def _introduce_typos(self, text):
        """
        Introduces random typos into a sentence.

        Args:
            text (str): The original sentence.

        Returns:
            str: Sentence with typos.
        """
        if len(text) < 2 or self._typo_count == 0:
            return text

        text_list = list(text)  # Convert string to mutable list
        for _ in range(self._typo_count):
            # Pick a random character index
            idx = random.randint(0, len(text_list)-1)
            # Replace with a random lowercase letter
            text_list[idx] = random.choice('abcdefghijklmnopqrstuvwxyz')
        return ''.join(text_list)  # Convert list back to string
     
    """"I will never spam my friends again."

        Length: 31 characters

        Typo count: 3

        Step 1: Pick Random Positions
        Randomly choose 3 positions to introduce typos:

        Position 3 → 'l' in "will"

        Position 11 → 's' in "spam"

        Position 25 → 'e' in "friends"

        Step 2: Replace with Random Letters

        Position 3 → 'l' → 'x' → "wixl"

        Position 11 → 's' → 'q' → "qpam"

        Position 25 → 'e' → 'z' → "friundz"

        Step 3: Resulting Sentence
        "I wixl never qpam my friundz again."
        Sentence now has 3 typos at random positions.

        Each call to _introduce_typos would produce different positions and letters, e.g.:
        "I will never spom my frionds again."
        or
        "I wjll never spqm my freinds again."
        """ 


    def generate_sentences(self):
        """
        Generates the list of punishment sentences with typos and numbering.

        Returns:
            List[str]: Numbered sentences with typos.
        """
        sentences = []
        for i in range(1, self._repetitions + 1):
            typo_sentence = self._introduce_typos(self._sentence)
            sentences.append(f"{i}. {typo_sentence}")
        return sentences
    
    """ I will never spam my friends again."
        Repetitions: 5

        Typo count: 2

        Step 1: Loop over repetitions
        The method loops from 1 to 5 (because repetitions = 5).

        Each loop iteration represents one numbered sentence.

        Numbering starts at 1.

        Step 2: Introduce typos
        For each iteration, _introduce_typos is called to randomly alter 2 characters.

        Example typos for each iteration:

        "I wjll never spam my friends again."

        'i' → 'j'

        'l' → 'l' (random choice, could be unchanged)

        "I will nevor spam my friends again."

        'e' → 'o'

        'r' → 'r'

        "I will nevbr spam my friends again."

        'e' → 'b'

        'v' → 'v'

        "I wjll never spqm my friends again."

        'i' → 'j'

        'a' → 'q'

        "I will never spam my friens again."

        'd' → 'n'

        'e' → 'e'

        Step 3: Number the sentence
        Each typo sentence is prepended with the line number:

       
        1. I wjll never spam my friends again.
        2. I will nevor spam my friends again.
        3. I will nevbr spam my friends again.
        4. I wjll never spqm my friends again.
        5. I will never spam my friens again.
        The numbering ensures it’s clear and ordered.

        Step 4: Collect into a list
        All 5 sentences are stored in a list:

        [
        "1. I wjll never spam my friends again.",
        "2. I will nevor spam my friends again.",
        "3. I will nevbr spam my friends again.",
        "4. I wjll never spqm my friends again.",
        "5. I will never spam my friens again."
        ]
        This list is what generate_sentences() returns."""

    # ---------- Display ----------
    def display(self):
        """Prints all generated punishment sentences."""
        all_sentences = self.generate_sentences()
        for line in all_sentences:
            print(line)

    # ---------- String Representation ----------
    def __str__(self):
        """Returns a summary string of the object."""
        return f"LinePunishmentWriter: '{self._sentence}' repeated {self._repetitions} times with {self._typo_count} typos per sentence"
