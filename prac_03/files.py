from time import process_time_ns

name = input("Enter your name: ")


def main():
    name_writer()
    file_reader()

    first_two_numbers = first_two_lines_of_numbers_txt()
    print(first_two_numbers)
    total = total_of_numbers_txt()
    print(total)




def name_writer():
    """Writes user input of name to name.txt"""
    in_file = open("name.txt", "w")
    in_file.write(name)
    in_file.close()


def file_reader():
    """Reads name.txt and adds a greeting"""
    in_file = open("name.txt", "r")
    print(f"Hi {in_file.read()}!")
    in_file.close()



def first_two_lines_of_numbers_txt():
    """Adds value of first 2 numbers of numbers.txt"""
    with open("numbers.txt", "r") as read_file:
        first_two_numbers = int(read_file.readline()) + int(read_file.readline())
        return first_two_numbers

def total_of_numbers_txt():
    """Adds total of all numbers in numbers.txt"""
    with open("numbers.txt", "r") as read_file:
        total = 0
        for line in read_file:
            total = total + int(line)

        return total
main()


