
class Guitar:
    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __repr__(self):
        return self.__str__()

    def get_age(self):
        guitar_age = 2024 - self.year
        return guitar_age

    def is_vintage(self):
        guitar_age = self.get_age()
        if guitar_age >= 50:
            return True
        else:
            return False

