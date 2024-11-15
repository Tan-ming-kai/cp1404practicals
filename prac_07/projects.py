import datetime


class Project:
    """ This class represents the different parts of the project """
    def __init__(self, name, start_date, priority=0, cost_estimate=0.0, percentage=0):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.percentage = percentage

    def project_is_completed(self):
        """checks if the project has been completed and returns a boolean accordingly"""
        if self.percentage == 100:
            return True
        else:
            return False

    def updated_percentage(self, updated_percentage):
        """updates the percentage completion of the project"""
        self.percentage = updated_percentage

    def __lt__(self, other):
        """logic for sorting the projects list by priority"""
        return self.priority < other.priority

    def __str__(self):
        """String representation for the display function"""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate}, completion: {self.percentage}%"

    def __repr__(self):
        return self.__str__()
