"""
project management
Estimate: 4 hours
Actual:
"""
from prac_07.projects import Project
from datetime import *

menu = """Menu:
- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""

print("Welcome to Pythonic Project Management")


def main():
    projects = extract_file_information()
    print(f"Loaded {len(projects)} projects from projects.txt")

    print(menu)
    user_choice = input(">>> ").upper()

    while user_choice != 'Q':

        if user_choice == 'L':
            print()
        elif user_choice == 'S':
            print()
        elif user_choice == 'D':

            completed_projects = []
            incomplete_projects = []
            for project in projects:
                if project.project_is_completed():
                    completed_projects.append(project)
                else:
                    incomplete_projects.append(project)

            print("Incomplete Projects:")
            for project in incomplete_projects:
                print(f"\t{project}")

            print("Completed Projects:")
            for project in completed_projects:
                print(f"\t{project}")
            # blank line after display function
            print()

        elif user_choice == 'F':
            print()
        elif user_choice == 'A':

            print("Let's add a new project")
            name = validates_name()
            new_date = validates_date()
            priority = validates_priority()
            cost_estimate = validates_cost_estimate()
            completion_percentage = validates_percentage()
            new_project = Project(name, new_date, priority, cost_estimate, completion_percentage)
            print(f"{new_project.name} added successfully")
            projects.append(new_project)

        elif user_choice == 'U':

            i = 1
            for project in projects:
                print(f"{i}. {project}")
                i += 1
            project_choice = validates_project_choice(projects)
            print(projects[project_choice-1])

            new_percentage = validates_percentage()
            projects[project_choice-1].updated_percentage(new_percentage)

        # end of user menu
        else:
            print(f"{user_choice} is not a valid option")
        print(menu)
        user_choice = input(">>> ").upper()

    print("Thank you for using custom-built project management software.")


def extract_file_information():
    """ Reads file information and stores in project_list"""
    projects = []
    with open("projects.txt", "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
        return projects


def validates_name():
    """validates project name input and only returns a name if it is not blank"""
    name = input("Name: ")
    if name:
        return name
    print("project name cannot be blank.")
    return validates_name()


def validates_date():
    """validates project date input and only returns it when it is in the correct format of (dd/mm/yyyy)"""
    new_date = input("start date (dd/mm/yyyy): ")
    try:
        datetime.strptime(new_date, "%d/%m/%Y")
        return date
    except ValueError:
        print("Invalid date format do it in (dd/mm/yyyy)")
        return validates_date()


def validates_priority():
    """validates project priority input and only returns it when it is a number more than 0"""
    try:
        priority = int(input("Priority: "))
        if priority > 0:
            return priority
        else:
            print("Priority must be more than 0.")
            return validates_priority()
    except ValueError:
        print("Invalid input, please enter a real number")
        return validates_priority()


def validates_cost_estimate():
    """validates project cost input and only returns it when it is a number more than 0"""
    try:
        cost_estimate = float(input("Cost estimate: "))
        if cost_estimate >= 0:
            return cost_estimate
        else:
            print("Cost cannot be less than 0")
            return validates_cost_estimate()
    except ValueError:
        print("Invalid input, please enter a real number")
        return validates_cost_estimate()


def validates_percentage():
    """validates project completion percentage input and only returns it when it is a number more than 0"""
    try:
        percentage = int(input("Enter completion percentage (0-100): "))
        if 0 <= percentage <= 100:
            return percentage
        else:
            print("Completion percentage must be between 0 and 100.")
            return validates_percentage()
    except ValueError:
        print("Invalid input, please enter a real number")
        return validates_percentage()


def validates_project_choice(projects):
    """validates project choice input and only returns it when it is a number more than 0"""
    try:
        project_choice = int(input("Project choice: "))
        if 0 < project_choice <= len(projects) :
            return project_choice
        else:
            print(f"Project choice must be between 1 and {len(projects)}")
            return validates_project_choice(projects)
    except ValueError:
        print("Invalid input, please enter a real number")
        return validates_project_choice(projects)

main()
