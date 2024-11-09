"""
project management
Estimate: 4 hours
Actual:
"""
from prac_07.projects import Project

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

            print("Incomplete Projects")
            for project in incomplete_projects:
                print(f"\t{project}")

            print("Completed Projects")
            for project in completed_projects:
                print(f"\t{project}")
            # blank line after display function
            print()

        elif user_choice == 'F':
            print()
        elif user_choice == 'A':
            print()
        elif user_choice == 'U':
            print()
        else:
            print(f"{user_choice} is not a valid option")
        print(menu)
        user_choice = input(">>> ").upper()

    print("Thank you for using custom-built project management software.")


def extract_file_information():
    """ Reads file information and stores in project_list"""
    project_list = []
    with open("projects.txt", "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            project_list.append(project)
        return project_list

main()
