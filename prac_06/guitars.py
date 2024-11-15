from prac_06.guitar import Guitar

def main():
    guitars = []
    print("My Guitars!")
    user_guitar_name = input("Name: ")

    while user_guitar_name != "":

        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: "))
        guitars.append(Guitar(user_guitar_name, guitar_year, guitar_cost))
        print(f"{user_guitar_name} ({guitar_year}): ${guitar_cost:.2f} added.")
        user_guitar_name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    i = 1
    for guitar in guitars:
        #
        # if guitar.is_vintage():
        #     vintage_string = "(Vintage)"
        # else:
        #     vintage_string = ""

        vintage_string = "(Vintage)" if guitar.is_vintage() else ""


        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")
        i += 1


main()