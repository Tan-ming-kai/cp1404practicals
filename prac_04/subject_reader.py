"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"



def main():
    data = load_data()
    print(data) #part 2 of question
    print() #empty line
    display_details(data) #part 3


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        data.append(parts)
    input_file.close()
    return data


def display_details(data):
    """displays details of each course"""
    for course in data:
        print(f"{course[0]} is taught by {course[1]} and has {course[2]} students")



main()