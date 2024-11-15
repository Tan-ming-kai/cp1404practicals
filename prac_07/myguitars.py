from prac_07.guitar import Guitar


def main():
    """contains the main function of the program"""
    guitars = reads_guitar_csv_file()

    # sorts the guitars list with the __lt__ method
    guitars.sort()

    for guitar in guitars:
        print(guitar)

    # adding a new guitar
    user_guitar_name = input("Name of your guitar: ")
    user_guitar_year = int(input("Year of your guitar: "))
    user_guitar_cost = float(input("Cost of your guitar: "))
    user_guitar = [Guitar(user_guitar_name, user_guitar_year, user_guitar_cost)]
    guitars.append(user_guitar)
    guitars.sort()

    with open("guitars.csv", "a") as guitars_file:
        print(f"{user_guitar_name},{user_guitar_year},{user_guitar_cost}", file=guitars_file)


def reads_guitar_csv_file():
    """reads guitar.csv file and returns it into a list"""
    guitars = []
    in_file = open('guitars.csv', 'r')

    # stores each line as a separate object of the Guitar class
    for line in in_file:
        parts = line.strip().split(',')
        guitar = [Guitar(parts[0], int(parts[1]), float(parts[2]))]
        guitars.append(guitar)
    in_file.close()
    return guitars


main()
