class WordFrequencyCounter:
    """
    A simple word frequency counter.

    This class counts the occurrences of words in a given text. 
    Words should be separated by spaces. 
    """

    def __init__(self, text_content:str):

        """ Attributes:
       - _text_content (str): The original text content.
       - _frequencies (dict): A dictionary storing word frequencies."""
        
        # Validate the input before storing it
        # - Ensures text_content is a string
        # - Prevents invalid data from being stored in the object
        # - Keeps internal state consistent and safe
        # - Provides immediate error reporting if input is invalid
        self._validate_text_content(text_content)

        #copy constructor
        if isinstance(text_content,WordFrequencyCounter):
            self._text_content=text_content._text_content
        else:
            self._text_content = text_content
            self._frequencies = {} # Initialize empty frequency dictionary

    @property
    def text_content(self):
        return self._text_content
    
    @text_content.setter
    def text_content(self,new_text):
        self._validate_text_content(new_text)
        self._text_content=new_text

    @property
    def frequencies(self):
        return self._frequencies


    def _validate_text_content(self,text_content):
        if not isinstance(text_content,str):
            raise TypeError("Input must be string only")

    def process_text(self):
        """
        Process the text and count the frequency of each word.

        The text is converted to lowercase and split by spaces.
        Frequencies are storedin the `_frequencies` dictionary.
        """
        # Convert text to lowercase and split into words
        text = self.text_content.lower().split()

         # Count word occurrences
        for word in text:
            if word in self.frequencies:
                self.frequencies[word] += 1
            else:
                self.frequencies[word] = 1

    def __str__(self):
        result = "Word Frequency Counter:\n"
        for word, count in self.frequencies.items():
            result += f"{word}: {count}\n"
        return result.strip()
