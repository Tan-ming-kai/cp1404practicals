class ProgrammingLanguages:

    def __init__(self, language_name="", typing="", reflection="", year=0):
        self.language_name = language_name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.language_name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def __repr__(self):
        return self.__str__()

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        else:
            return False
