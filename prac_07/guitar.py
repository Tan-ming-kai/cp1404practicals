
class Guitar:
    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __repr__(self):
        """string representation of the information in the guitar class"""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __lt__(self, other):
        """logic for sorting guitars by year"""
        return self.year < other.year

    def get_age(self):
        """gets the age of the guitar"""
        guitar_age = 2024 - self.year
        return guitar_age

    def is_vintage(self):
        """checks if the guitar is over 50 years old """
        guitar_age = self.get_age()
        if guitar_age >= 50:
            return True
        else:
            return False


