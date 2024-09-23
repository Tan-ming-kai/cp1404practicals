get_user_password = input("Enter your password with at least 10 characters: ")

while len(get_user_password) < 10:
    print("Your password must contain at least 10 characters.")
    get_user_password = input("Enter your password with at least 10 characters: ")

starred_password = "*" * len(get_user_password)
print(starred_password)