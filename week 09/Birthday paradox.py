import random

class BirthdayParadox:
    def __init__(self,group_size,simulations=100):
        """
        Initialize the simulation with:
        - group_size: number of people in the group
        - simulations: number of times to repeat the experiment
        """
        self.group_size=group_size
        self.simulations=simulations

    def make_birthdays(self):
        """
        Generate random birthdays for the group.
        Each birthday is represented as an integer 0..364 
        """
        birthdays = [] #will store birthdays here
        for i in range(self.group_size):
            day = random.randint(1, 365)  # pick a random day 
            birthdays.append(day)
        return birthdays

    def detect_duplicates(self, birthdays):
        """
        Check if the given list of birthdays contains duplicates.
        Returns True if at least two people share the same birthday,
        otherwise returns False.
        """
        size=len(birthdays)
        for i in range(size): #[100,200,34,100,29] it will take the first value 100
            for j in range(i + 1,size): # it will take the second value cuz it has to check that if there's any duplicate or not
                if birthdays[i] == birthdays[j]: # 100==200?,100==34,100==56,100==100
                    return True   # found duplicate
        return False              # no duplicates

    def run(self):
        """
        Run the simulation multiple times (self.simulations).
        Each run generates birthdays for the group and checks 
        for duplicates. 
        Returns the probability (as a fraction) that at least 
        two people share a birthday.
        """
        occurences = 0   # counts how many times duplicates occurred
        for i in range(self.simulations):
            birthdays = self.make_birthdays() # generate group birthdays
            if self.detect_duplicates(birthdays):
                occurences += 1 # increment if duplicate found
        probability = occurences / self.simulations
        return probability

    def show_probability(self): 
        probablity=self.run()   
        print(f"For {self.group_size} people → Probability ≈ {probablity:.3f}")
