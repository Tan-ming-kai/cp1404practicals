import datetime


class Project:
    def __init__(self, name, start_date, priority=0, cost_estimate=0.0, percentage=0):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.percentage = percentage

    def project_is_completed(self):
        if self.percentage == 100:
            return True
        else:
            return False

    def updated_percentage(self, updated_percentage):
        self.percentage = updated_percentage

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate}, completion: {self.percentage}%"

    def __repr__(self):
        return self.__str__()
