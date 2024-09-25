def main():


MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()


def convert_to_fahrenheit():
    get_celsius = float(input("Celsius: "))
    get_fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def convert_to_celsius():
    get_fahrenheit = float(input("Fahrenheit: "))
    get_celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


while choice != "Q":
    if choice == "C":
        fahrenheit = convert_to_fahrenheit()
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        convert_to_celsius()
        celsius = convert_to_celsius()
        print(f"Result: {celsius:.2f} C")

        # Hint: celsius = 5 / 9 * (fahrenheit - 32)
        # Remove the "pass" statement when you are done. It's a placeholder.
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")