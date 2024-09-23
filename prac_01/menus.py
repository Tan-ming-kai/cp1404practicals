name =input("Enter your name: ")
menu = """H - Hello
G - Goodbye
Q - Quit
>>>"""
print(menu)
user_choice = input("Enter your choice: ").upper()

while user_choice != "Q":
    if user_choice == "H":
        print(f"HELLO {name}")
    elif user_choice == "G":
        print(f"Goodbye {name}")
    else:
        print(f"{user_choice} is not a valid option")
    print(menu)
    user_choice = input("Enter your choice: ").upper()
print("Finished")