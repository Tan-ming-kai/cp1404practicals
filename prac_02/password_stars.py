def main():
    get_user_password = user_password()

    asterisk_password(get_user_password)


def asterisk_password(get_user_password):
    starred_password = "*" * len(get_user_password)
    print(starred_password)


def user_password():
    get_user_password = input("Enter your password with at least 10 characters: ")
    while len(get_user_password) < 10:
        print("Your password must contain at least 10 characters.")
        get_user_password = input("Enter your password with at least 10 characters: ")
    return get_user_password


main()


