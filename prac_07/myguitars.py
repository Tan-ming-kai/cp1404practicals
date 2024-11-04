from prac_07.guitar import Guitar


def main():
    guitars = reads_guitar_csv_file()
    guitars.sort()

    for guitar in guitars:
        print(guitar)


def reads_guitar_csv_file():
    """reads guitar.csv file and returns it into a list"""
    guitars = []
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()
    return guitars


main()
