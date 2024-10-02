
name = input("Enter your name: ")


def main():
    name_writer()
    file_reader()
    numbers_txt_file_reader()




def name_writer():
    in_file = open("name.txt", "w")
    in_file.write(name)
    in_file.close()


def file_reader():
    in_file = open("name.txt", "r")
    print(f"Hi {in_file.read()}!")
    in_file.close()



def numbers_txt_file_reader():
    with open("numbers.txt", "r") as read_file:
        first_two_lines = read_file.readlines()
        first_two_numbers = int(first_two_lines[0]) + int(first_two_lines[1])
        print(first_two_numbers)



main()


