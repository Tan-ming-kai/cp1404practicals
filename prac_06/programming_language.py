class ProgrammingLanguages:

    def __init__(self, language="", typing="", reflection="", year=0):
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f""

    def __repr__(self):
        return self.__str__()

    def is_dynamic(self):
        if self.typing == "DYNAMIC":
            return True
        else:
            return False
