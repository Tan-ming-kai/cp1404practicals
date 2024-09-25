def main():
    MENU = """    C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit = convert_to_fahrenheit()
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            celsius = convert_to_celsius()
            print(f"Result: {celsius:.2f} C")

            # Hint: celsius = 5 / 9 * (fahrenheit - 32)
            # Remove the "pass" statement when you are done. It's a placeholder.
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")



def convert_to_fahrenheit():
    get_celsius = float(input("Celsius: "))
    get_fahrenheit = get_celsius * 9.0 / 5 + 32
    return get_fahrenheit


def convert_to_celsius():
    get_fahrenheit = float(input("Fahrenheit: "))
    get_celsius = 5 / 9 * (get_fahrenheit - 32)
    return get_celsius


main()
