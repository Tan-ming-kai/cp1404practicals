name = input("Enter your name: ")


def main():
    name_writer()
    file_reader()



def name_writer():
    in_file = open("name.txt", "w")
    in_file.write(name)
    in_file.close()


def file_reader():
    in_file = open("name.txt", "r")
    print(f"Hi {in_file.read()}")
    in_file.close()
main()

