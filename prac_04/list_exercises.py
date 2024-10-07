def main():
    numbers = []
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface','BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer','bob']

    numbers = get_user_numbers(numbers)
    print(numbers)
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers)/len(numbers)}")
    print()

    username_validity = username_checker(usernames)

    if username_validity:
        print("username is valid")
    else:
        print("username is invalid")



def get_user_numbers(numbers):
    """gets user numbers and appends to a list"""
    for i in range(0,5):
        user_number = int(input("Enter a number: "))
        numbers.append(user_number)
    return numbers

def username_checker(usernames):
    """checks if the username inputted is present in the list of usernames"""
    username_validity = False
    user_username = input("Enter a username: ")

    for username in usernames:
        if user_username == username:
            username_validity = True
            return username_validity
        else:
            username_validity = False

    return username_validity




main()