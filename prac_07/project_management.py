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
- (Q)uit
"""

print("Welcome to Pythonic Project Management")
def main():


    projects = extract_file_information()
    print(f"Loaded {len(projects)} projects from projects.txt")

    print(menu)
    user_choice = ""
    while user_choice != 'Q':
        user_choice = input("Choose an option: ").strip().upper()

        if user_choice == 'L':
            print()
        elif user_choice == 'S':
            print()
        elif user_choice == 'D':
            print("Incomplete Projects")
            for project in projects:
                print(f"\t{project}")
        elif user_choice == 'F':
            print()
        elif user_choice == 'A':
            print()
        elif user_choice == 'U':
            print()
        else:
            print(f"{user_choice} is not a valid option")
            # end of program
    print("Thank you for using custom-built project management software.")



def extract_file_information():
    project_list = []
    with open("projects.txt", "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            project_list.append(project)
        return project_list


main()

