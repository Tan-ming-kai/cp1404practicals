name = input("Enter your name: ")


def main():
    name_writer()



def name_writer():
    in_file = open("name.txt", "w")
    in_file.write(name)
    in_file.close()

main()


