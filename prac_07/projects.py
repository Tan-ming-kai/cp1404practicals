
class Project:
    def __init__(self, name="", date="", priority=0, cost_estimate=0.0, percentage=0):
        self.name = name
        self.date = date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.percentage = percentage

    def __str__(self):
        return f"{self.name}, start: {self.date}, priority {self.priority}, estimate: ${self.cost_estimate}, completion: {self.percentage}%"

    # Organise Pantry, start: 20/07/2022, priority 1, estimate: $25.00, completion: 55%

    def __repr__(self):
        return self.__str__()

    def add_project(self):
        print()

    def project_is_completed(self):
        completed_projects = []
        incomplete_projects = []
        if self.percentage == 100:
            return True

